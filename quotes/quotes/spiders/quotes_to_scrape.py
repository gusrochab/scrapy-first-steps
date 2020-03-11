# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class QuotesToScrapeSpider(scrapy.Spider):
    name = 'quotes_to_scrape'
    allowed_domains = ['http://quotes.toscrape.com/js/']

    script = '''
        function main(splash, args)
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(1))
            return splash:html()
        end  
    '''

    def start_requests(self):
        yield SplashRequest(url='http://quotes.toscrape.com', callback=self.parse, endpoint='execute',
                            args={'lua_source': self.script})

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'quote': quote.xpath(".//span[@class='text']/text()").get(),
                'author': quote.xpath(".//span/small/text()").get()
            }

