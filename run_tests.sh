#!/usr/bin/env bash

set -u

if [ -f ".venv/Scripts/activate" ]; then
    source ".venv/Scripts/activate"
elif [ -f ".venv/bin/activate" ]; then
    source ".venv/bin/activate"
else
    echo "Virtual environment not found: .venv/Scripts/activate or .venv/bin/activate"
    exit 1
fi

python -m pytest -q

exit $?