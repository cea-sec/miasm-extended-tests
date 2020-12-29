#!/bin/sh
set -e
for test_file in test_flags_x86_32 test_flags_x86_64 test_flags_arm test_flags_mips32 test_flags_aarch64; do
	python test_flags.py $test_file
done
