# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import csv
import traceback

import pymysql


class MySQLPipeline:

    def __init__(self, connection):
        self.connection = connection

    @classmethod
    def from_settings(cls, settings):
        db_config = {
            "host": settings["DB_HOST"],
            "db": settings["DB_NAME"],
            "port": settings.get("DB_PORT", 3306),
            "user": settings["DB_USER"],
            "password": settings["DB_PWD"],
            "charset": 'utf8'
        }
        return cls(pymysql.connect(**db_config))

    def process_item(self, item, spider):
        sql = "insert into maoyan (`name`,category,show_time) value (%s, %s, %s)"
        try:
            with pymysql.cursors.SSCursor(self.connection) as cursor:
                cursor.execute(sql, (item.get("title"), item.get("category"), item.get("show_time")))
                self.connection.commit()
        except:
            spider.logger.exception(traceback.format_exc())
            self.connection.rollback()

    def close_spider(self, spider):
        if self.connection:
            self.connection.close()

