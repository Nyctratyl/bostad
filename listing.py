from datetime import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class Listing:
    id: int
    publish_date: datetime
    street_address: str
    floor: Optional[float]
    description: str
    asking_price: Optional[int]
    fee: Optional[int]
    living_area: float
    coordinates: (float, float)
    slug: str

    def __repr__(self):
        s = f"{self.street_address}, {self.asking_price} kr, {self.living_area} kvm"
        if self.floor is not None:
            s += f" vån {self.floor}"
        return s
    
    def link(self) -> str:
        return "https://www.hemnet.se/bostad/" + self.slug