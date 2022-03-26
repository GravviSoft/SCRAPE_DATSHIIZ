import scrapy


class Bit2Spider(scrapy.Spider):
    name = 'BIT2'
    allowed_domains = ['ndt.com']
    start_urls = ['http://ndt.com/']

    def parse(self, response):
        pass
