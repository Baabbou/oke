#!/bin/bash

if [ "$UID" -ne 0 ]; then
    echo "You must run this script as root user."
    exit 1
fi 

python -m venv .venv
source .venv/bin/activate
.venv/bin/pip install -r requirements.txt

pyinstaller --onefile --clean oke.py

cp dist/oke /usr/bin/oke 
cp dist/oke /usr/local/bin/oke

rm -rf oke.spec build dist .venv  

echo " "
echo "Oke was correctly installed in /usr/bin/oke and /usr/local/oke"
