import scrapy


class YelpSpider(scrapy.Spider):
    name = 'YELP'
    allowed_domains = ['ndt.com']
    start_urls = ['http://ndt.com/']

    def parse(self, response):
        pass
