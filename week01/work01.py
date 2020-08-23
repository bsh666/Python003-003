# -*- coding:utf-8 _*-
"""
    电影名称、电影类型和上映时间

    `python work01.py`
"""
import re
import os
import sys
import csv
import time
import random
import logging
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup as bs

headers = {
    'accept': ("text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,"
               "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"),
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    # 'cookie': "uuid_n_v=v1; uuid=02090D40E53011EA9E4093FE69325283A220E0EC5A5E4904ACD4C517AEF3BA81; _csrf=c58d7bd5b0989e94ad29bf2aa80799abd68c9520fc14ad325832759d68ff1cda; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598180504; _lxsdk_cuid=1741afb32e8c8-06fcd80171c8e8-31647305-1fa400-1741afb32e9c8; _lxsdk=02090D40E53011EA9E4093FE69325283A220E0EC5A5E4904ACD4C517AEF3BA81; mojo-uuid=f2919df793e4ab4b6fb14eb4f146641a; mojo-session-id={\"id\":\"004f1c571680c022108b067563c3b036\",\"time\":1598180504806}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598180507; __mta=119878455.1598180504451.1598180504451.1598180506644.2; _lxsdk_s=1741afb32e9-db3-272-1ee%7C%7C4",
    'host': "maoyan.com",
    'sec-fetch-dest': "document",
    'sec-fetch-mode': "navigate",
    'sec-fetch-site': "cross-site",
    'sec-fetch-user': "?1",
    'upgrade-insecure-requests': "1",
    'user-agent': ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36")
}

homepage = "https://maoyan.com/films?showType=3"

date_compile = re.compile(r"\d{4}-\d{2}-\d{2}(?: \d{2}:\d{2})?")

csv_file = "movies_by_requests.csv"
heads = ["name", "category", "show time"]

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)

logger = logging.getLogger(__name__)
logger.setLevel(10)


def make_soup(url):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = bs(response.text, "lxml")
    time.sleep(random.randrange(5, 8))
    return soup


def write(data):
    with open(os.path.join(current_path, csv_file), "w") as w:
        writer = csv.writer(w)
        writer.writerow(heads)
        writer.writerows(data)


def crawl():
    soup = make_soup(homepage)
    items = soup.find_all("div", attrs={"class": "movie-item"})
    logger.info(f"Fetched {len(items)} items.")
    details = []
    for item in items:
        link = item.find("a")["href"]
        logger.info(link)
        url = urljoin(homepage, link)
        detail = handle_detail(url)
        if detail is None:
            break
        details.append(detail)
        if len(details) == 10:
            break
    return details


def handle_detail(link):
    soup = make_soup(link)
    brief_container = soup.select_one("div.movie-brief-container")
    if brief_container is None:
        logger.warning("Fetching detail failed.")
        return
    title = brief_container.select_one("h1").get_text(strip=True)
    details = brief_container.select("ul>li")
    category, date = parse_detail(details)
    logger.debug(f"{title}, {category}, {date}")
    return title, category, date


def parse_detail(tags):
    cat_tag, *_, date_tag = tags
    cat_text = ",".join([tag.get_text(strip=True) for tag in cat_tag.find_all("a")])
    date_regx = date_compile.search(date_tag.get_text(strip=True))
    date_string = date_regx.group() if date_regx else ""
    return cat_text, date_string


def run():
    data = crawl()
    write(data)


if __name__ == '__main__':
    run()
