# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import csv


class Work02Pipeline:
    file_name = "movies_by_scrapy.csv"
    heads = ["name", "category", "show time"]

    def __init__(self):
        self.file_handler = open(self.local_storage, "w")
        self.writer = csv.writer(self.file_handler)

    def open_spider(self, spider):
        self.writer.writerow(self.heads)

    def process_item(self, item, spider):
        self.writer.writerow(item.values())
        return item

    @property
    def local_storage(self):
        return os.path.join(
            os.path.abspath(
                os.path.dirname(
                    os.path.dirname(os.path.dirname(__file__)))),
            self.file_name)

    def close_spider(self, spider):
        self.file_handler.close()