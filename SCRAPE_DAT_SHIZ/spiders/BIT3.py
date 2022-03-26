import scrapy


class Bit3Spider(scrapy.Spider):
    name = 'BIT3'
    allowed_domains = ['ndt.com']
    start_urls = ['http://ndt.com/']

    def parse(self, response):
        pass
