import os
import json
from haversine import haversine
from tunnelbana import *
from listing import *
from parsers import *
import datetime

def parse_from_data_dir() -> list[Listing]:
    DATA_PATH = "./data"
    DESIRED_TUNNELBANA = [
        MARIATORGET,
        HORNSTULL,
        ZINKENSDAMM,
        MEDBORGARPLATSEN,
        SLUSSEN,
        SKANSTULL
    ]

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

        #print(address)
        coords = listing_card["coordinates"]
        #print(listing_card["publishedAt"])
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
        #print("==============")


    #print("PARSE DONE")
    RES = []
    for listing in LISTINGS:
        if listing.asking_price is None or listing.asking_price > 5000000:
            continue
        if listing.floor is None or listing.floor < 3:
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
    for res in links:
        print(res.link())
