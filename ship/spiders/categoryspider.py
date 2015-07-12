import scrapy

from ship.items import CategoryItem

class CategorySpider(scrapy.Spider):
	"""docstring for CategorySpider"""

	name = "catspider"
	allowed_domains = ["shipspotting.com"]
	page_url = "http://www.shipspotting.com"
	start_urls = [
		page_url + "/gallery/categories.php"
	]

	def parse(self, response):
		cats = response.xpath('//td[@class="whiteboxstroke"]/a')
		file = open('categories.txt', 'a')

		for cat in cats:
			item = CategoryItem()

			item['name'] = cat.xpath('img/@title').extract()[0]
			item['link'] = cat.xpath('@href').extract()[0]

			link = item['link']
			sid = link[link.index('=')+1:len(link)]
			str = sid + '|' + item['name'] + '\n'

			file.write(str)

			yield item

		file.close()