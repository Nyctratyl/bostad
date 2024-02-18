#!/bin/bash
./scrape.sh
source .venv/bin/activate
python notify.py
