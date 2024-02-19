#!/bin/bash
PAGES=$(curl 'https://www.hemnet.se/bostader?location_ids[]=18031' | grep 'role="presentation">...</span>.*hcl-pagination-button' -o | grep 'page=[0-9]*' -o | cut -c -5 --complement)
BUILDID=$(curl -s https://www.hemnet.se/bostader | grep "buildId.*isFallback" -o | cut -c -10 --complement | rev | cut -c -13 --complement | rev)
for ((page=1; page<$PAGES; page++))
do
    echo "scraping, page: ${page}"
    curl -s "https://www.hemnet.se/_next/data/${BUILDID}/bostader.json?location_ids[]=18031&page=${page}" > ./data/page_nr_${page}.json
done