import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re
import os


def scrap():
    with open("test.html", "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, features="html.parser")
        soup = soup.body

        walk_div_maze = [
            ("h-root", 0),
            ("div", 0),
            ("h-shell", 0),
            ("div", 0),
            ("main", 0),
            ("div", 0),
            ("h-main-content", 0),
            ("div", 0),
            ("h-grid-page", 0),
            ("div", 0),
            ("div", 2), # now we going into the grid
            ("div", 0),
            ("h-grid-results", 0),
            ("ul", 0)  # under ul we have li!!!!
        ]

        for div_name, child_loc in walk_div_maze:
            soup = [e for e in soup.children if e.name == div_name][child_loc]


        # take a peak at next level
        items = [e for e in soup.children if e.name == "li"]

        print(first_stuff.name)
        print(first_stuff.text)
        print()



if __name__ == "__main__":
    scrap()
