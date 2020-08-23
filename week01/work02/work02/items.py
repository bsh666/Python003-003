# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import re

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join

date_compile = re.compile(r"\d{4}-\d{2}-\d{2}(?: \d{2}:\d{2})?")


def filter_time(value):
    date_regx = date_compile.search(value)
    return date_regx.group() if date_regx else ""


def strip(value):
    return [v.strip() for v in value]


class Work02Item(scrapy.Item):
    title = scrapy.Field(
        output_processor=TakeFirst()
    )
    category = scrapy.Field(
        input_processor=strip,
        output_processor=Join(separator=",")
    )
    show_time = scrapy.Field(
        input_processor=MapCompose(filter_time),
        output_processor=TakeFirst()
    )

