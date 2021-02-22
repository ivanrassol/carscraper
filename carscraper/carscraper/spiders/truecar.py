import scrapy
from scrapy.loader import ItemLoader
from carscraper.items import TruecarItem


class TruecarSpider(scrapy.Spider):
    name = 'truecar'
    start_urls = ['https://www.truecar.com//']

    def parse(self, response):
        brands_urls = [
            #'https://www.truecar.com/new-cars-for-sale/listings/dodge/',
            #'https://www.truecar.com/new-cars-for-sale/listings/ferrari/,
            #'https://www.truecar.com/new-cars-for-sale/listings/lamborghini/',
            #'https://www.truecar.com/new-cars-for-sale/listings/nissan/',
            'https://www.truecar.com/used-cars-for-sale/listings/dodge/',
            'https://www.truecar.com/used-cars-for-sale/listings/ferrari/',
            'https://www.truecar.com/used-cars-for-sale/listings/lamborghini/',
            'https://www.truecar.com/used-cars-for-sale/listings/nissan/'
        ]

        yield from response.follow_all(brands_urls, self.parse_cars, headers=response.headers)

    def parse_cars(self, response):
        for car in response.css('div.vehicle-card-body'):
            loader = ItemLoader(item=TruecarItem(), selector=car)
            loader.add_css('make', 'span.vehicle-header-make-model::text')
            loader.add_css('model', 'span.vehicle-header-make-model::text')
            loader.add_css('year', 'span.vehicle-card-year::text')
            loader.add_css(
                'price', 'div[data-test="vehicleCardPricingBlockPrice"]::text')
            yield loader.load_item()

        yield from response.follow_all(
            css='a[data-test="Pagination-directional-next"]',
            callback=self.parse_cars,
            headers=response.headers
        )
