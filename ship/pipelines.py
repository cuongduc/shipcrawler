# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from PIL import Image
from cStringIO import StringIO
import re

class ShipImagesPipeline(ImagesPipeline):
	
	CONVERTED_ORIGINAL = re.compile('^full/[0-9,a-f]+.jpg$')

	def get_media_requests(self, item, info):
		print "get_media_requests"

		return [Request(x, meta={'image_names': item["image_name"]})
				for x in item.get('image_urls', [])]

	# Extract image from response
	def get_images(self, response, request, info):
		print "get_images"

		for key, image, buf, in super(ShipImagesPipeline, self).get_images(response, request, info):
			if self.CONVERTED_ORIGINAL.match(key):
				key = self.change_filename(key, response)
			yield key, image, buf

	def change_filename(self, key, response):
		return "full/%s.jpg" % response.meta['image_names'][0]