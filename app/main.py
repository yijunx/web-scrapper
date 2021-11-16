import time
from scrapper import scrap
from schemas import Item


def parse_string_into_item(
    list_item_text: str
) -> Item:

    pass


def main():
    # run the script to pull to index html

    # get contents from html
    print("scrapping")
    scrap()


if __name__ == "__main__":
    while True:
        main()
        time.sleep(4)
