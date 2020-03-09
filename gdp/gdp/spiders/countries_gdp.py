# -*- coding: utf-8 -*-
import scrapy


class CountriesGdpSpider(scrapy.Spider):
    name = 'countries_gdp'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['http://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        print('#'*30)
        countries = response.xpath('//tbody/tr')
        for country in countries:
            name = country.xpath('.//td[1]/a/text()').get()
            gdp = country.xpath('.//td[2]/text()').get()
            
            yield {'name': name,
                    'gdp': gdp}

