# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field
from itemloaders.processors import TakeFirst, Compose, Join


class TruecarItem(Item):
    make = Field(input_processor=TakeFirst())
    model = Field(input_processor=Compose(lambda x: x[1:], Join(), lambda y: y.strip()))
    year = Field()
    price = Field()

#TODO: add itemloader for Truecar new cars

class AutotraderItem(Item):
    make = Field()
    model = Field()
    year = Field()
    price = Field()