import time
from scrapper import scrap
from schemas import Item
import subprocess
import os
from email_handler import send_email_alert
from datetime import datetime
from typing import Dict, List


RUN: int = 0
CURRENT_SET_OF_ITEMS: dict = {}
HTML_PATHS: List[str] = [
    "to_parse_sg.html",
    "to_parse_hk.html",
    "to_parse_fr.html",
    "to_parse_uk.html"
]


def parse_string_into_item(list_item_text: str) -> Item:
    """
    list_item_text: "Cabas H en Biais 40 bag, Color:  pink ,  S$ 5,000"
    """
    # update to normal space first
    list_item_text = list_item_text.replace("\xa0", " ")
    try:
        name_part, color_part, price_part = list_item_text.split(", ")
        color = color_part.split(":")[1]
        currency, quantity = price_part.strip().split(" ")

        return Item(
            item_name=name_part.strip(),
            item_color=color.strip(),
            item_price_quantity=quantity.strip(),
            item_price_currency=currency.strip(),
        )
    except ValueError:
        return None


def pull():
    print("pulling")
    subprocess.run(["bash", "app/fetch.sh"])


def compare(was_dict: Dict[str, Item], is_dict: Dict[str, Item]):
    if RUN == 0:
        # well it is first run... just pass
        print("FIRST RUN!!")
    else:
        new_item_names = [x for x in is_dict if x not in was_dict]
        new_items = [is_dict[x] for x in new_item_names]
        if new_items:
            print("GOT NEW ITEMS TO SEND!!!!")
            send_email_alert(items=new_items)
        else:
            print("NOTHING TO SEND!!!")


def start():
    # run the script to pull to index html
    global RUN
    global CURRENT_SET_OF_ITEMS

    # this pull, pulls all html files 
    pull()

    # get contents from html
    for html_path in HTML_PATHS:
        web_items = scrap(html_path)
        items = [parse_string_into_item(x) for x in web_items]
        lastest_set_of_items = {}
        for item in items:
            if item is not None and item.item_name not in lastest_set_of_items:
                lastest_set_of_items[item.item_name] = item

        compare(was_dict=CURRENT_SET_OF_ITEMS, is_dict=lastest_set_of_items)

    # for k, v in lastest_set_of_items.items():
    #     print(k)
    #     print(v)
    #     print()

    RUN += 1
    CURRENT_SET_OF_ITEMS = lastest_set_of_items


if __name__ == "__main__":
    while True:
        print(f"====== Starting a run on {datetime.now()} ======")
        start()
        # need to run the bash script
        time.sleep(int(os.getenv("INTERNAL_IN_SECONDS")))
