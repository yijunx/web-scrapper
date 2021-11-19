import time
from scrapper import scrap
from schemas import Item
import subprocess


# here is some nasty glocal vars...
RUN: int = 0
CURRENT_SET_OF_ITEMS: dict = {}


def parse_string_into_item(
    list_item_text: str
) -> Item:
    """
    list_item_text: "Cabas H en Biais 40 bag, Color:  pink ,  S$ 5,000"
    """
    # update to normal space first
    list_item_text = list_item_text.replace(u'\xa0', u' ')
    try:
        name_part, color_part, price_part = list_item_text.split(', ')
        color = color_part.split(":")[1]
        currency, quantity = price_part.strip().split(" ")

        return Item(
            item_name = name_part.strip(),
            item_color = color.strip(),
            item_price_quantity = quantity.strip(),
            item_price_currency = currency.strip()
        )
    except ValueError:
        return None

    
def pull():
    print("pulling")
    subprocess.run(["bash", "app/fetch.sh"]) 
    pass
    

def start():
    # run the script to pull to index html
    pull()

    # get contents from html
    web_items = scrap()
    items = [parse_string_into_item(x) for x in web_items]
    item_dict = {}
    for item in items:
        if item is not None and item.item_name not in item_dict:
            item_dict[item.item_name] = item.dict()
    
    # for k, v in item_dict.items():
    #     print(k)
    #     print(v)
    #     print()


if __name__ == "__main__":
    start()
    # while True:
    #     main()
    #     # need to run the bash script
    #     time.sleep(4)
