from typing import Optional
import re
import logging

def parse_floor(floor: str) -> Optional[float]:
    logging.debug(floor)
    if floor is None:
        return None
    
    if "/" in floor:
        floor = floor[:floor.index("/")]
    if "vån " in floor:
        floor = floor.replace("vån ", "")
    floor = floor.replace(",", ".")
    return float(floor)
    

def parse_asking(asking: str) -> Optional[int]:
    try:
        return int(asking[:-3].replace('\xa0', ''))
    except:
        return None

def parse_fee(fee: str) -> Optional[float]:
    try:
        return float(fee[:-7].replace('\xa0', ''))
    except:
        return None

def parse_living_area(living_area: str) -> Optional[float]:
    try:
        living_area = living_area[:-3]
        if "+" in living_area:
            living_area = living_area.split("+")[0]
        return float(living_area.replace(',', '.'))
    except:
        return None

def parse_coords(coords: dict) -> tuple[float, float]:
    return (coords["lat"], coords["long"])