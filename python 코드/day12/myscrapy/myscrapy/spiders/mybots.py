# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import MyscrapyItem

class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['naver.com']
    start_urls = ['https://section.blog.naver.com/PowerBlog.nhn?currentPage=1']

    def parse(self, response):
        print(response)
        # titles = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a/text()').extract()
        # authors = response.css('.writing::text').extract()
        # previews = response.css('.lede::text').extract()

        # items = []
        # # loop 
        # for idx in range(len(titles)):
        #     item = MyscrapyItem()
        #     item['title'] = titles[idx]
        #     item['author'] = authors[idx]
        #     item['preview'] = previews[idx]

        #     items.append(item)

        # return items
        pass
