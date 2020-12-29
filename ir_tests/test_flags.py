from __future__ import print_function
import sys
from future.utils import viewvalues
from miasm.ir.ir import IRBlock, AssignBlock
from miasm.analysis.binary import Container
from miasm.analysis.machine import Machine
from miasm.core.locationdb import LocationDB
from miasm.analysis.simplifier import IRCFGSimplifierSSA
from miasm.expression.simplifications import expr_simp
from miasm.expression.expression import (
    ExprInt,
    ExprId,
    ExprLoc,
    ExprSlice,
    ExprMem,
    ExprOp,
    ExprCompose,
)


arg0_32 = ExprId("arg0_32", 32)
arg1_32 = ExprId("arg1_32", 32)
arg2_32 = ExprId("arg2_32", 32)
arg3_32 = ExprId("arg3_32", 32)

arg0_64 = ExprId("arg0_64", 64)
arg1_64 = ExprId("arg1_64", 64)


args_x86_32 = {
    ExprMem(ExprId("ESP", 32) + ExprInt(0x4, 32), 32): arg0_32,
    ExprMem(ExprId("ESP", 32) + ExprInt(0x8, 32), 32): arg1_32,
    ExprMem(ExprId("ESP", 32) + ExprInt(0xC, 32), 32): arg2_32,
    ExprMem(ExprId("ESP", 32) + ExprInt(0x10, 32), 32): arg3_32,
}

args_x86_64 = {
    ExprId("RDI", 64): arg0_64,
    ExprId("RSI", 64): arg1_64,
}

args_arm = {
    ExprId("R0", 32): arg0_32,
    ExprId("R1", 32): arg1_32,
    ExprId("R2", 32): arg2_32,
    ExprId("R3", 32): arg3_32,
}

args_aarch64 = {
    ExprId("X0", 64): arg0_64,
    ExprId("X1", 64): arg1_64,
}

args_mips32 = {
    ExprId("A0", 32): arg0_32,
    ExprId("A1", 32): arg1_32,
    ExprId("A2", 32): arg2_32,
    ExprId("A3", 32): arg3_32,
}


def reduce_arguments_x86_32_args64(expr_simp, expr):
    expr = expr.replace_expr(
        {
            ExprCompose(arg1_32, arg0_32): arg0_64,
            ExprCompose(arg3_32, arg2_32): arg1_64,
        }
    )
    return expr


def reduce_arguments_x86_32_args64(expr_simp, expr):
    expr = expr.replace_expr(
        {
            ExprCompose(arg1_32, arg0_32): arg0_64,
            ExprCompose(arg3_32, arg2_32): arg1_64,
        }
    )
    return expr


def reduce_arguments_aarch64_32(expr_simp, expr):
    expr = expr.replace_expr(
        {
            arg0_64[:32]: arg0_32,
            arg1_64[:32]: arg1_32,
        }
    )
    return expr


# Add simplification pass to replace arguments
expr_simp.enable_passes(
    {
        ExprCompose: [
            reduce_arguments_x86_32_args64,
        ],
        ExprSlice: [
            reduce_arguments_aarch64_32,
        ],
    }
)

i32_0 = ExprInt(0, 32)
i64_0 = ExprInt(0, 64)

# Test conditions
test_conditions = {
    "test_s32_pos_or_equal": [ExprOp("<s", arg0_32, i32_0)],
    "test_s32_neg": [ExprOp("<s", arg0_32, i32_0)],
    "test_s32_greater": [
        ExprOp("<=s", arg0_32, arg1_32),
        ExprOp("<s", arg1_32, arg0_32),
    ],
    "test_s32_greater_or_equal": [ExprOp("<s", arg0_32, arg1_32)],
    "test_s32_lesser": [ExprOp("<s", arg0_32, arg1_32)],
    "test_s32_lesser_or_equal": [
        ExprOp("<=s", arg0_32, arg1_32),
        ExprOp("<s", arg1_32, arg0_32),
    ],
    "test_u32_greater": [
        ExprOp("<=u", arg0_32, arg1_32),
        ExprOp("<u", arg1_32, arg0_32),
    ],
    "test_u32_greater_or_equal": [ExprOp("<u", arg0_32, arg1_32)],
    "test_u32_lesser": [ExprOp("<u", arg0_32, arg1_32)],
    "test_u32_lesser_or_equal": [
        ExprOp("<=u", arg0_32, arg1_32),
        ExprOp("<u", arg1_32, arg0_32),
    ],
    "test_s64_pos": [
        ExprOp("<s", arg0_64, i64_0),
        ExprOp("<s", arg1_32, i32_0),
        ExprOp("<s", arg0_32, i32_0),
    ],
    "test_s64_neg": [
        ExprOp("<s", arg0_64, i64_0),
        ExprOp("<s", arg1_32, i32_0),
        ExprOp("<s", arg0_32, i32_0),
    ],
    "test_s64_greater": [
        ExprOp("<=s", arg0_64, arg1_64),
        ExprOp("<s", arg1_64, arg0_64),
        ExprOp("<s", arg2_32, arg0_32),
    ],
    "test_s64_greater_or_equal": [
        ExprOp("<s", arg0_64, arg1_64),
        ExprOp("<s", arg0_32, arg2_32),
    ],
    "test_s64_lesser": [
        ExprOp("<s", arg0_64, arg1_64),
        ExprOp("<s", arg0_32, arg2_32),
    ],
    "test_s64_lesser_or_equal": [
        ExprOp("<=s", arg0_64, arg1_64),
        ExprOp("<s", arg1_64, arg0_64),
        ExprOp("<s", arg2_32, arg0_32),
    ],
    "test_u64_greater": [
        ExprOp("<=u", arg0_64, arg1_64),
        ExprOp("<u", arg1_64, arg0_64),
        ExprOp("==", arg1_32, arg3_32),
        ExprOp("<u", arg2_32, arg0_32),
    ],
    "test_u64_greater_or_equal": [
        ExprOp("<u", arg0_64, arg1_64),
        ExprOp("==", arg1_32, arg3_32),
        ExprOp("<u", arg0_32, arg2_32),
    ],
    "test_u64_lesser": [
        ExprOp("<u", arg0_64, arg1_64),
        ExprOp("==", arg1_32, arg3_32),
        ExprOp("<u", arg0_32, arg2_32),
    ],
    "test_u64_lesser_or_equal": [
        ExprOp("<=u", arg0_64, arg1_64),
        ExprOp("<u", arg1_64, arg0_64),
        ExprOp("==", arg1_32, arg3_32),
        ExprOp("<u", arg2_32, arg0_32),
    ],
}

for filename in sys.argv[1:]:
    print("File: %s" % filename)
    fdesc = open(filename, "rb")

    loc_db = LocationDB()
    cont = Container.from_stream(fdesc, loc_db)
    machine = Machine(cont.arch)
    mdis = machine.dis_engine(cont.bin_stream, loc_db=cont.loc_db)
    lifter = machine.lifter_model_call(mdis.loc_db)
    fake_head = mdis.loc_db.add_location("fake_head")

    for func_name in [
        "test_s32_pos_or_equal",
        "test_s32_neg",
        "test_s32_greater",
        "test_s32_greater_or_equal",
        "test_s32_lesser",
        "test_s32_lesser_or_equal",
        "test_u32_greater",
        "test_u32_greater_or_equal",
        "test_u32_lesser",
        "test_u32_lesser_or_equal",
        "test_s64_pos",
        "test_s64_neg",
        "test_s64_greater",
        "test_s64_greater_or_equal",
        "test_s64_lesser",
        "test_s64_lesser_or_equal",
        "test_u64_greater",
        "test_u64_greater_or_equal",
        "test_u64_lesser",
        "test_u64_lesser_or_equal",
    ]:
        head = mdis.loc_db.get_name_location(func_name)
        addr = mdis.loc_db.get_location_offset(head)
        asmcfg = mdis.dis_multiblock(addr)

        ircfg = lifter.new_ircfg_from_asmcfg(asmcfg)
        # Add fake head
        dct = {lifter.IRDst: ExprLoc(head, lifter.IRDst.size)}
        dct.update(args_x86_32)
        dct.update(args_x86_64)
        dct.update(args_arm)
        dct.update(args_aarch64)
        dct.update(args_mips32)

        assignblk = AssignBlock(dct, None)
        irblock = IRBlock(loc_db, fake_head, [assignblk])
        # print(irblock)
        ircfg.add_irblock(irblock)

        open("ircfg_%s.dot" % func_name, "w").write(ircfg.dot())

        simplifier = IRCFGSimplifierSSA(lifter)

        ircfg = simplifier.simplify(ircfg, fake_head)
        open("result_%s.dot" % func_name, "w").write(ircfg.dot())

        # Get first block
        irblock = ircfg.blocks[fake_head]
        dst = irblock.dst
        print("%-30s %s" % (func_name, dst))
        assert dst.is_cond()
        cond = dst.cond
        test_condition = test_conditions[func_name]
        assert cond in test_condition
