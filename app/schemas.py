from typing import List
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    color: str
    price: str


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
