# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SkiiItem(scrapy.Item):
    # define the fields for your item here like:

    # The name and size of the skii
    name = scrapy.Field()
    # The price of the skii
    price = scrapy.Field()

    pass
