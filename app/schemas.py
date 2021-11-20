from typing import List
from pydantic import BaseModel


class Item(BaseModel):
    item_name: str
    item_color: str
    item_price_quantity: str
    item_price_currency: str


class NewItemsOfLocation(BaseModel):
    location: str
    url: str
    items: List[Item]


class NewItemsOfLocations(BaseModel):
    data: List[NewItemsOfLocation]


class LocationInfo(BaseModel):
    location: str
    html_path: str
    url: str


class LocationsInfo(BaseModel):
    data: List[LocationInfo]
