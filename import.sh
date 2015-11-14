#!/bin/sh
source ./venv/bin/activate

if [ "$#" -ne 1 ]
then
    echo "A region parameter is expected."
else
    python import.py --regions $1
fi