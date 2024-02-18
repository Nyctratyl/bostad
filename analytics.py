from listing import *
from parse import *

listings = parse_from_data_dir()
for listing in listings:
    if "kammakargatan" in listing.slug:
        print(listing)