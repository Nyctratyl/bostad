#!/bin/bash
cd /home/pi/code/bostad
echo "RUNNING SCRAPE"
echo $(date)
./scrape.sh
echo "SCRAPE DONE"
source .venv/bin/activate
echo "RUNNING PARSE/NOTIFY"
python notify.py
echo "NOTIFY DONE"
echo "================"
