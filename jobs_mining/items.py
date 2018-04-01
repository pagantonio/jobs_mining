# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class JobItem(Item):
    title = Field()
    company = Field()
    location = Field()
    state_short = Field()
    state_long = Field()
    country = Field()
    short_summary = Field()
    long_summary = Field()
    tag = Field()
    source = Field()
