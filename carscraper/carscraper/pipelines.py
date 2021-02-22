# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3


class CarscraperPipeline:
    def __init__(self):
        self.db = 'test.sqlite'
        self.table = 'data'
        self.conn = sqlite3.connect(self.db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS {table} (make TEXT, model TEXT, year TEXT, price TEXT)".format(table=self.table))

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO {table} VALUES(?,?,?,?);".format(
            table=self.table), (item['make'][0], item['model'][0], item['year'][0], item['price'][0]))
        self.conn.commit()
        return item
