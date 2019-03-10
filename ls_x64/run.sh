#!/bin/sh

MIASM_DIR="$1"

python $MIASM_DIR/example/jitter/run_with_linuxenv.py -v -f "alh" -- ls
