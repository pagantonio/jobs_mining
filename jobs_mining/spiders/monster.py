# -*- coding: utf-8 -*-
import scrapy


class MonsterSpider(scrapy.Spider):
    name = "monster"
    allowed_domains = ["monster.com"]
    start_urls = ['http://monster.com/']

    def parse(self, response):
        pass
