#!/bin/bash

set -e
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

echo "Run venv/bin/python main.py"