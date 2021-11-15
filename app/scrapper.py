import pandas as pd
import numpy as np
from urllib.request import urlopen, Request, FancyURLopener  # to open the website
from bs4 import BeautifulSoup
import re
import os
import requests

session = requests.Session()


class AppURLopener(FancyURLopener):
    # version = "Mozilla/5.0"
    version = "fancybrowser2.43"




def scrap():
    url = os.getenv("SCRAPPING_URL")
    url = "https://www.hermes.com/sg/en/category/women/bags-and-small-leather-goods/bags-and-clutches"
    headers = {
        "User-Agent": "zzz"
    }

    
    # req = Request(url=url, headers=headers)
    # html = urlopen(req)
    # opener = AppURLopener()
    # response = opener.open(url)
    # soup = BeautifulSoup(html)
    # print(response.fp.read())
    response = session.get(url, headers=headers)
    print(response.status_code)


if __name__ == "__main__":
    scrap()
