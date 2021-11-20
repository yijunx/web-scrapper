import time
from schemas import (
    LocationInfo,
    LocationsInfo,
    NewItemsOfLocation,
    NewItemsOfLocations,
)
from scrapper import scrap
from schemas import Item
import subprocess
import os
from email_handler import send_email_alert
from datetime import datetime
from typing import Dict, List


CURRENT_SET_OF_ITEMS: Dict[str, dict] = {}
LOCATIONS_INFO = LocationsInfo(
    data=[
        LocationInfo(
            location="sg",
            url=os.getenv("SCRAPPING_URL_SG"),
            html_path="to_parse_sg.html",
        ),
        LocationInfo(
            location="uk",
            url=os.getenv("SCRAPPING_URL_UK"),
            html_path="to_parse_uk.html",
        ),
        LocationInfo(
            location="hk",
            url=os.getenv("SCRAPPING_URL_HK"),
            html_path="to_parse_hk.html",
        ),
        LocationInfo(
            location="fr",
            url=os.getenv("SCRAPPING_URL_FR"),
            html_path="to_parse_fr.html",
        ),
    ]
)


def parse_string_into_item(list_item_text: str) -> Item:
    """
    list_item_text: "Cabas H en Biais 40 bag, Color:  pink ,  S$ 5,000"
    """
    # update to normal space first
    list_item_text = list_item_text.replace("\xa0", " ")
    try:
        name_part, color_part, price_part = list_item_text.split(", ")
        color = color_part.split(":")[1]

        return Item(
            name=name_part.strip(),
            color=color.strip(),
            price=price_part.strip(),
        )
    except ValueError as e:
        # print(f"THERE IS VALUE ERROR IN PARSING STRING {list_item_text}")
        # print(str(e))
        return None


def pull():
    print("pulling")
    subprocess.run(["bash", "app/fetch.sh"])


def compare(is_dict: Dict[str, Item], was_dict: Dict[str, Item] = None) -> List[Item]:
    if was_dict is None:
        # well it is first run... just pass
        # print("FIRST RUN!!")
        return []
    else:
        new_item_names = [x for x in is_dict if x not in was_dict]
        new_items = [is_dict[x] for x in new_item_names]
        return new_items


def start():
    # run the script to pull to index html
    global CURRENT_SET_OF_ITEMS

    # this pull, pulls all html files of all location
    pull()

    # get contents from html
    new_items_of_locations = NewItemsOfLocations(data=[])

    need_to_send = False

    for location_info in LOCATIONS_INFO.data:
        web_items = scrap(
            html_path=location_info.html_path, location=location_info.location
        )
        items = [parse_string_into_item(x) for x in web_items]
        lastest_set_of_items_of_location = {}
        for item in items:
            if item is not None and item.name not in lastest_set_of_items_of_location:
                lastest_set_of_items_of_location[item.name] = item

        new_items_of_location = compare(
            was_dict=CURRENT_SET_OF_ITEMS.get(location_info.location, None),
            is_dict=lastest_set_of_items_of_location,
        )

        if new_items_of_location:
            need_to_send = True
            # print(f"THERE ARE NEW STUFF ON {location_info.location} !!!")
            # print(f"THEY ARE:")
            # print(new_items_of_location)
            # print()
        new_items_of_locations.data.append(
            NewItemsOfLocation(
                location=location_info.location,
                url=location_info.url,
                items=new_items_of_location,
            )
        )

        CURRENT_SET_OF_ITEMS[location_info.location] = lastest_set_of_items_of_location

    if need_to_send:
        send_email_alert(new_items_of_locations=new_items_of_locations)
    # else:
    #     print("NOTHING NEW, NO NEED TO SEND")


if __name__ == "__main__":
    while True:
        print(f"====== Starting a run on {datetime.now()} ======")
        start()
        # need to run the bash script
        time.sleep(int(os.getenv("INTERNAL_IN_SECONDS")))
