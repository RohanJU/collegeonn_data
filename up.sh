#!/bin/sh
# usage: ./up.sh [batchfile]  -> rebuild UP output; report on that batch (or all)
cd "$(dirname "$0")"
if [ -n "$1" ]; then S=$(python3 -c "import json,sys;print(' '.join(json.load(open(sys.argv[1]))))" "$1"); fi
SRC=up-colleges-to-fill-2026-09-26.csv OUT=up-colleges-filled.csv DATA=data_up python3 build.py $S
