from urllib.parse import urljoin

import scrapy
from scrapy.loader import ItemLoader

from week02.work01.work01.items import Work01Item


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    headers = {
        'accept': ("text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,"
                   "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"),
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cache-control': "no-cache",
        'connection': "keep-alive",
        'host': "maoyan.com",
        'sec-fetch-dest': "document",
        'sec-fetch-mode': "navigate",
        'sec-fetch-site': "cross-site",
        'sec-fetch-user': "?1",
        'referer': 'https://maoyan.com/films',
        'upgrade-insecure-requests': "1",
        'user-agent': ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36")
    }

    def start_requests(self):
        start_url = "https://maoyan.com/films"
        yield scrapy.Request(start_url, headers=self.headers)

    def parse(self, response, **kwargs):
        links = response.xpath(
            "//div[@class='movie-item film-channel']//a[starts-with(@href, '/film')]/@href").getall()
        if not links:
            self.logger.critical("未解析到链接，可能已触发反爬.")
        links = links[:5] if len(links) >= 5 else links
        for link in links:
            yield scrapy.Request(
                urljoin(response.url, link), headers=self.headers, callback=self.parse_detail)

    def parse_detail(self, response):
        print(response.request.meta.get("proxy"))
        selector = response.xpath("//div[@class='movie-brief-container']")
        loader = ItemLoader(Work01Item(), selector=selector)
        loader.add_xpath("title", "./h1/text()")
        loader.add_xpath("category", "./ul/li/a/text()")
        loader.add_xpath("show_time", "./ul/li[3]/text()")
        return loader.load_item()
