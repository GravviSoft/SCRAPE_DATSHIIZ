import scrapy


class BitSpider(scrapy.Spider):
    name = 'BIT'
    allowed_domains = ['ndt.com']
    start_urls = ['http://ndt.com/']

    def parse(self, response):
        pass
