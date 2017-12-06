# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    """
    伯乐在线blog的爬虫
    """
    name = 'jobbole_blog'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/']

    def parse(self, response):
        print(response.body.text)
        with open("blog.txt","w") as fi:
            fi.write(response.body.text)
