import scrapy


class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['www.amazon.in']
    start_urls = ['http://www.amazon.in/']

    def parse(self, response):
        print("thsi si sthe ")
