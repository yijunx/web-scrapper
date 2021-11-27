from collections import defaultdict
from bs4 import BeautifulSoup


default_maze_walker = [
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
    ("div", 2),  # now we going into the grid
    ("div", 0),
    ("h-grid-results", 0),
    ("ul", 0),  # under ul we have li!!!!
]

_special_maze_walker = {}


def scrap(html_path: str, location: str, debug_mode: bool = False):
    print(f"Scrapping {html_path}")
    with open(html_path, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, features="html.parser")
        soup = soup.body

        walk_div_maze = _special_maze_walker.get(location, None)
        if walk_div_maze is None:
            walk_div_maze = default_maze_walker

        divs_passed = []
        for div_name, child_loc in walk_div_maze:
            divs_passed.append(div_name)
            try:
                soup = [e for e in soup.children if e.name == div_name][child_loc]
            except Exception as e:
                print(str(e))
                print(f"we are in div path: {divs_passed}, trying to get children...")
                try:
                    print([x.name for x in soup.children if x.name is not None])
                except Exception as exc:
                    print(f"getting children failed with {str(exc)}")
                    return []
                return []

        # take a peak at next level (NICE!)
        if debug_mode:
            print([e.text for e in soup.children if e.name is not None][0])
            item_strings = []
        else:
            item_strings = [e.text for e in soup.children if e.name == "li"]
    # return item_strings
    return item_strings


if __name__ == "__main__":
    scrap(html_path="to_parse_uk", location="uk", debug_mode=True)
