import time
import logging
import requests
from bs4 import BeautifulSoup


# each district is an Item
class Item:
    def __init__(self, lk: str, n: str, c: str):
        self.link = lk
        self.name = n
        self.code = c

    def __str__(self):
        return self.link + self.name + self.code


# this region is for debugging
log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename="spider.log", level=logging.DEBUG, format=log_format)


def debug(s: str, logg: bool = True, console: bool = True, exc: bool = False):
    if exc:
        print(s)
        logging.warning(s)
    elif console:
        print(s)
        logging.info(s)
    elif logg:
        logging.info(s)
    else:
        logging.debug(s)


def dfs_from(link: str, layer: int):
    suc = False
    while not suc:
        try:
            time.sleep(0.11)
            r = requests.get(link, timeout=2)
            suc = True
        except:
            debug(f"Exception! in requests, layer: {layer}, link: {link}", exc=True)
            time.sleep(0.51)

    r.encoding = "GB18030"

    obs = BeautifulSoup(r.text, "html.parser")

    all_links = obs.find_all("a")
    will = []

    for every_link in all_links:
        if every_link.has_attr("href"):
            new_link: str = every_link.attrs["href"]
            title: str = every_link.contents[0]

            if title.find("ICP") == -1 and not title.isdigit():
                will.append(Item(base(link) + new_link, title, link_to_code(new_link)))

    debug(f"proceeding... layer: {layer}, link: {link}", console=(layer <= 3))

    if len(will) == 0:
        if not read_node(obs, layer):
            debug(f"Exception! in read_node, layer: {layer}, link: {link}", exc=True)
            time.sleep(0.51)
            dfs_from(link, layer)
    else:
        if r.text.find("<td>市辖区</td>") != -1:
            print("\t" * layer + encode(link_to_raw(link) + "01") + "市辖区", file=output_file)
        for w in will:
            print("\t" * layer + w.code + w.name, file=output_file)
            dfs_from(w.link, layer + 1)


def read_node(obs: BeautifulSoup, layer: int) -> bool:
    tbl = obs.find_all("table", class_="villagetable")
    if len(tbl) == 0:
        return False

    tr = tbl[0].find_all("tr", class_="villagetr")

    for item in tr:
        td = item.find_all("td")
        print("\t" * layer + td[0].string + td[2].string + td[1].string, file=output_file)

    return True


def link_to_code(link: str) -> str:
    return encode(link_to_raw(link))


def base(link: str) -> str:
    i = link.rfind("/")
    link = link[: i + 1]
    return link


def site(link: str) -> str:
    i = link.rfind("/")
    link = link[i + 1:]
    return link


def link_to_raw(link: str) -> str:
    link = site(link).replace(".html", "")
    return link


def encode(code: str) -> str:
    aim = len("110100000000")
    while len(code) < aim:
        code += '0'
    return code


base_link: str = r"http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2020/"

with open("xxx_StatData.txt", "w") as output_file:
    dfs_from(base_link, 0)
