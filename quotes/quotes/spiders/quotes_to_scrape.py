# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import cv2

class QuotesToScrapeSpider(scrapy.Spider):
    name = 'quotes_to_scrape'
    allowed_domains = ['http://quotes.toscrape.com/js/']

    script = '''
        function main(splash, args)
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(1))
            return splash:png()
        end  
    '''

    def start_requests(self):
        s = SplashRequest(url='http://quotes.toscrape.com', callback=self.parse, endpoint='execute',
                            args={'lua_source': self.script}, dont_process_response=False)
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n')
        print(type(s))
        print('\n')
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n')
        yield s

    def parse(self, response):
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n')
        print(type(response))
        print('\n\n\n')
        print('RESPONSE.BODY\n')
        print(response.body)
        print('\n\n\n')
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n')
        yield response

        '''
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'quote': quote.xpath(".//span[@class='text']/text()").get(),
                'author': quote.xpath(".//span/small/text()").get()
            }
        '''
