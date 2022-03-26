import scrapy


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['ndt.com']
    start_urls = ['http://ndt.com/']

    def parse(self, response):
        pass
