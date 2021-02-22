import scrapy
import extruct
from scrapy.loader import ItemLoader
from carscraper.items import AutotraderItem
from pprint import pprint

class AutotraderSpider(scrapy.Spider):
    name = 'autotrader'

    start_urls = [
        'https://www.autotrader.com/cars-for-sale/all-cars/dodge/beverly-hills-ca-90210?dma=&searchRadius=25&location=&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=25',
        'https://www.autotrader.com/cars-for-sale/all-cars/ferrari/beverly-hills-ca-90210?dma=&searchRadius=25&location=&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=25',
        'https://www.autotrader.com/cars-for-sale/all-cars/nissan/beverly-hills-ca-90210?dma=&searchRadius=25&location=&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=25',
        'https://www.autotrader.com/cars-for-sale/all-cars/dodge/beverly-hills-ca-90210?dma=&searchRadius=25&location=&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=25'
    ]

    urls_to_append = []

    #TODO: Find a better stop condition.
    for url in start_urls:
        for n in range(25, 101, 25):
            urls_to_append.append(f'{url}&firstRecord={n}')

    start_urls.extend(urls_to_append)

    def parse(self, response):
        pass
        cars = extruct.extract(response.text, uniform=True)['json-ld'][2:]

        for car in cars:
            loader = ItemLoader(item=AutotraderItem())
            loader.add_value('make', car['brand']['name'])
            loader.add_value('model', car['model'])
            loader.add_value('year', car['productionDate'])
            loader.add_value('price', car['offers']['price'])
            yield loader.load_item()