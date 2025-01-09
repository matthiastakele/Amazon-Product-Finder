import json
import scrapy
from urllub.parse import urljoin
import re

class AmazonSearchProductSpider(scrapy.Spider):
    name = "amazon_search_product"
    
    def start_requests(self):
        keyword_list = ['ipad']
        for keyword in keyword_list:
            url = f"https://www.amazon.com/s?k={keyword}&page=1"
            yield scrapy.Request(url=url, callback=self.discover_product_urls, meta={'keyword': keyword, 'page': 1})
            
    def discover_product_urls(self, response):
        page = response.meta['page']
        keyword = response.meta['keyword']
        
        search_products = response.css('div.s-result-item[data-component-type="s-search-result"]')
        for product in search_products:
            relative_url = product.css