import scrapy


class FbookSpider(scrapy.Spider):
    name = 'FBOOK'
    allowed_domains = ['ndt.com']
    start_urls = ['http://ndt.com/']

    def parse(self, response):
        pass
