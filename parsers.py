from typing import Optional
import re

def parse_floor(floor: str) -> Optional[float]:
    if floor is None:
        return None
    format_1 = re.findall("\d/\d", floor)
    if len(format_1) == 1:
        return float(format_1[0][0])
    if "-" in floor:
        return float(floor[4:6])
    return float(floor[4])
    

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