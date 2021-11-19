from pydantic import BaseModel


class Item(BaseModel):
    item_name: str
    item_color: str
    item_price_quantity: str
    item_price_currency: str
