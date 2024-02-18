from listing import *
from parse import *

listings = parse_from_data_dir()
listings = filter_listings(listings)
listings = sorted(listings, key=lambda listing : listing.publish_date)
for listing in listings:
    print(listing.street_address)
    print(listing.publish_date)