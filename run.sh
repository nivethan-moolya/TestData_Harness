#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
echo $SCRIPT_DIR
echo "fileName: $1";
for py_file in $(find $SCRIPT_DIR -name $1.py)
do
    python $py_file
done