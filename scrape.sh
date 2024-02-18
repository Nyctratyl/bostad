#!/bin/bash
for page in {1..49}
do
    echo "scraping, page: ${page}"
    curl -s "https://www.hemnet.se/_next/data/c2HT-Zoku_fJGOv-ygdmH/bostader.json?location_ids[]=18031&page=${page}" > ./data/page_nr_${page}.json
done