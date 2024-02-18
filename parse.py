import os
import json
from haversine import haversine
from tunnelbana import *
from listing import *
from parsers import *
import datetime
import logging

logging.basicConfig(level=logging.WARNING)

def parse_from_data_dir() -> list[Listing]:
    DATA_PATH = "./data"


    filenames = os.listdir(DATA_PATH)
    LISTING_CARDS = []
    for filename in filenames:
        file = open(f'{DATA_PATH}/{filename}').read()
        file_data = json.loads(file)
        listing_cards = [ x[1] for x in filter(lambda x : x[0].startswith("ListingCard"),
            file_data['pageProps']['__APOLLO_STATE__'].items()
            )]

        LISTING_CARDS = LISTING_CARDS + listing_cards


    LISTINGS: list[Listing] = []
    for listing_card in LISTING_CARDS:
        address = listing_card["streetAddress"]
        if False and "Kammakargatan 44" in address:
            logging.getLogger().setLevel(level=logging.DEBUG)
        logging.debug(address)
        listing = Listing(
            id = listing_card["id"],
            publish_date=datetime.datetime.fromtimestamp(float(listing_card["publishedAt"])),
            street_address=address,
            floor=parse_floor(listing_card["floor"]),
            description=listing_card["description"],
            asking_price=parse_asking(listing_card["askingPrice"]),
            fee=parse_fee(listing_card["fee"]),
            living_area=parse_living_area(listing_card["livingAndSupplementalAreas"]),
            coordinates=parse_coords(listing_card["coordinates"]),
            slug=listing_card["slug"]
        )

        LISTINGS = LISTINGS + [listing]
        logging.debug("==============")
        logging.getLogger().setLevel(level=logging.WARNING)
    return LISTINGS



def filter_listings(listings: list[Listing]):
    DESIRED_TUNNELBANA = SÖDER + ÖSTERMALM + CENTRUM
    RES = []
    for listing in listings:
        if listing.asking_price is None or listing.asking_price > 5000000:
            continue
        if listing.floor is None or listing.floor < 2:
            continue
        if listing.living_area is None or listing.living_area < 50:
            continue
        if not any(
            list(
                map(lambda tbana : haversine(listing.coordinates, tbana) < 0.5, DESIRED_TUNNELBANA)
            )
        ):
            continue

        RES = RES + [listing]

    RES = sorted(RES, key=lambda x : x.living_area)
    return RES


if __name__ == "__main__":
    links = parse_from_data_dir()
    links = filter_listings(links)
    for res in links:
        print(res.link())
