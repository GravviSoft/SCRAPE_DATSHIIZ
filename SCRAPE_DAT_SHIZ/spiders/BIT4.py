import scrapy


class Bit4Spider(scrapy.Spider):
    name = 'BIT4'
    allowed_domains = ['ndt.com']
    start_urls = ['http://ndt.com/']

    def parse(self, response):
        pass
