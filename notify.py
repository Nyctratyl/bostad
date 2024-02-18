from parse import *
from listing import *
from requests import post

def notify(listing: Listing):
    post("https://batsign.me/at/jacob.schoerner@gmail.com/5afe946d8e", listing.link())
    print(listing.link())
    return

links_file = open('seen_links', mode='r')
seen_links = links_file.read().split('\n')
links_file.close()
current_listings = parse_from_data_dir()
current_listings = filter_listings(current_listings)
for listing in current_listings:
    if listing.link() not in seen_links:
        notify(listing)
        seen_links.append(listing.link())

links_file = open('seen_links', mode='w')
links_file.write('\n'.join(seen_links))
links_file.close()