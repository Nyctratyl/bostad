from listing import *
from parse import *

listings = parse_from_data_dir()
print(f"Total n of listings: {len(listings)}")
listings = filter_listings(listings)
listings = sorted(listings, key=lambda listing : listing.publish_date)
if False:
    for listing in listings:
        print(listing.street_address)
        print(listing.publish_date)
        print("=====")