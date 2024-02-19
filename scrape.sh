#!/bin/bash
BUILDID=$(curl -s https://www.hemnet.se/bostader | grep "buildId.*isFallback" -o | cut -c -10 --complement | rev | cut -c -13 --complement | rev)
for page in {1..49}
do
    echo "scraping, page: ${page}"
    curl -s "https://www.hemnet.se/_next/data/${BUILDID}/bostader.json?location_ids[]=18031&page=${page}" > ./data/page_nr_${page}.json
done