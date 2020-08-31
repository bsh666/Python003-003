# -*- coding:utf-8 -*-
import os
import re
import random
import sys
import traceback
from _socket import timeout
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from requests.exceptions import Timeout, ProxyError, ConnectionError
from requests import HTTPError
from scrapy.cmdline import execute

FREE_PROXY_SOURCE = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt"


def _parse_text(text):
    if not text:
        return
    content, describe, *_ = text.split(" ")
    if describe[3] == "N":
        return
    scheme = "https" if describe.endswith("S") else "http"
    return f"{scheme}://{content}"


def _verify(proxy):
    url = urlparse(proxy)
    try:
        requests.get(f"{url.scheme}://www.baidu.com", proxies={url.scheme: proxy}, timeout=3)
        return proxy
    except (Timeout, ProxyError, ConnectionError, timeout):
        pass


def _fetch_free_proxies():
    response = requests.get(FREE_PROXY_SOURCE)
    response.raise_for_status()
    content = re.split(r"\n{2,}", response.text)[1]
    proxy_text_list = content.split("\n")
    proxies = list(filter(lambda x: x, [_parse_text(text) for text in proxy_text_list]))
    random.shuffle(proxies)
    available_proxies = []
    with ThreadPoolExecutor(min(len(proxies), 30)) as executor:
        tasks = [executor.submit(_verify, proxy) for proxy in proxies]
    for task in as_completed(tasks):
        proxy = task.result()
        if proxy is not None:
            available_proxies.append(proxy)
    with open(os.path.join("proxies.txt"), "w") as w:
        w.write("\n".join(available_proxies))


def main():
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(current_path)
    try:
        _fetch_free_proxies()
    except HTTPError:
        traceback.print_exc()
    execute(["scrapy", "crawl", "maoyan"])


if __name__ == '__main__':
    main()