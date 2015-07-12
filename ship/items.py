# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ShipItem(scrapy.Item):
    name 		= scrapy.Field()
    imo 		= scrapy.Field()
    category 	= scrapy.Field()
    image_urls  = scrapy.Field()
    images  	= scrapy.Field()
    image_name	= scrapy.Field()
    
class CategoryItem(scrapy.Item):
	name = scrapy.Field()
	link = scrapy.Field()