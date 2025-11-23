#!/bin/bash

echo "1. Removing venv folder...";
rm -rf venv;

echo "2. Creating venv folder...";
python3 -m venv venv;

echo "3. Activating venv...";
source venv/bin/activate;

echo "4. Installing dependencies...";
pip install --quiet --requirement requirements.txt;