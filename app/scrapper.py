import pandas as pd
import numpy as np
from urllib.request import urlopen, Request, FancyURLopener  # to open the website
from bs4 import BeautifulSoup
import re
import os
import requests

session = requests.Session()

# well scrapper failed but curl works


class AppURLopener(FancyURLopener):
    # version = "Mozilla/5.0"
    version = "fancybrowser2.43"




def scrap():
    url = os.getenv("SCRAPPING_URL")
    url = "https://www.hermes.com/sg/en/category/women/bags-and-small-leather-goods/bags-and-clutches"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh-TW;q=0.6,zh;q=0.5",
        "cache-control": "max-age=0",
        "Cookie": "_gid=GA1.2.1931154062.1636981860; _fbp=fb.1.1636981859669.1621585377; ECOM_SESS=v3s8m91vcik3smflpilihrrg67; correlation_id=e4e7d7419c68e160f1843ea74cb539ac459116faeb1374980d4fc9de9f5d7f08; _cs_mk=0.9495708899134336_1636983716183; _ga=GA1.2.906334706.1636981860; _ga_Y862HCHCQ7=GS1.1.1636983716.2.1.1636986040.0; datadome=aSYoLEEsz2GNZRtk77-Nvtq0COdtv-arYP7oC~oje-kaN3LXFJXcy-.yfnYnLBlDDTG1NhVJhO4IwgAQfimos2HGBTXedXVbXIN-a0.7AL",
        "If-None-Match": "W/\"6c49b-n/Cid5e8FNLR8Uv0VMjAew0pIhM",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"93\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"93\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-platform": "macOS",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1"
    }

    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15',
    #    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    #    'Accept-Encoding': 'none',
    #    'Accept-Language': 'en-US,en;q=0.8',
    #    'Connection': 'keep-alive'}

    
    req = Request(url=url, headers=headers)
    html = urlopen(req)
    print(html)
    # opener = AppURLopener()
    # response = opener.open(url)
    # print(response.read())
    # soup = BeautifulSoup(html)
    
    # response = session.get(url, headers={"User-Agent":"gozilla4.3"})
    # print(response.status_code)




if __name__ == "__main__":
    scrap()
