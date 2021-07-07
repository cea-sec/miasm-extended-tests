#!/bin/sh

MIASM_DIR="$1"

python $MIASM_DIR/example/jitter/simu_sc_linux.py -- chmod
python $MIASM_DIR/example/jitter/simu_sc_linux.py -- exec
