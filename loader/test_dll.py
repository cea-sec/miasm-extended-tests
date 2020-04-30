#! /usr/bin/env python

import os
import logging
from pdb import pm

from miasm.loader.pe_init import *
from miasm.loader.pe import *
from miasm.core.utils import *
from miasm.jitter.loader.pe import get_export_name_addr_list

log = logging.getLogger("test_dll")
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(levelname)-5s: %(message)s"))
log.addHandler(console_handler)
log.setLevel(logging.INFO)


def do_test(test_func):
    for root, dirs, files in os.walk('dll_win_xp'):
        for name in files:
            fname = os.path.join(root, name)
            log.info("Input: %s", fname)
            data = open(fname, 'rb').read()
            test_func(data)



def test_read_write(data):
    pe = PE(data)
    out = bytes(pe)
    new_pe = PE(out)

    exports_ref = get_export_name_addr_list(pe)
    exports_new = get_export_name_addr_list(new_pe)
    assert(len(exports_ref) == len(exports_new))

def test_move_resource(data):
    pe = PE(data)

    # Move resource description to new section
    s_res = pe.SHList.add_section(
        name="myres",
        rawsize=len(pe.DirRes)
    )
    pe.DirRes.set_rva(s_res.addr)

    out = bytes(pe)
    # Re parse PE
    new_pe = PE(out)


def test_move_import(data):
    pe = PE(data)
    if pe.NThdr.optentries[DIRECTORY_ENTRY_IMPORT].rva == 0:
        return
    # Move Import
    s_imp = pe.SHList.add_section(
        name="myimp",
        rawsize=len(pe.DirImport)
    )
    pe.DirImport.set_rva(s_imp.addr)

    out = bytes(pe)
    # Re parse PE
    new_pe = PE(out)

log.info("Test 1: read/write")
do_test(test_read_write)

log.info("Test 2: New resource section")
do_test(test_move_resource)

log.info("Test 2: New import section")
do_test(test_move_import)
