import scrapy

from ship.items import ShipItem

class ShipSpider(scrapy.Spider):
	"""docstring for ShipSpider"""

	LIMIT_START = 480000
	LIMIT_STOP	= 560000
	LIMIT_STEP 	= 192

	def drange(start, stop, step):
		r = start
		while r <= stop:
			yield r
			r += step

	name = "testshipspider"

	limit = ["%d" % x for x in drange(LIMIT_START,LIMIT_STOP,LIMIT_STEP)]

	allowed_domains = ["shipspotting.com"]
	page_url = "http://www.shipspotting.com"
	start_urls = [
		"http://www.shipspotting.com/gallery/search.php?limit=192&limitstart=%s"\
		"&search_manager=&sortkey=p.lid&sortorder=desc&page_limit=192&viewtype=2"\
		% x for x in limit
	]

	def parse(self, response):
		ships = response.xpath("//tr/td[@class='whiteboxstroke']")
		file = open('val.txt', 'a')

		for ship in ships:
			item = ShipItem()
			
			name 	 = ship.xpath('table/tr/td[contains(@scope, "col")]/a/img/@alt').extract()[0]
			category = ship.xpath('table/tr/td[contains(@style,"font-size:9pt;")]/a[contains(@href,"search_category_1")]/@href').extract()[0]
			url      = ship.xpath('table/tr/td[contains(@scope, "col")]/a/img/@src').extract()[0].replace('small', 'middle')

			href	 = ship.xpath('table/tr/td[contains(@scope, "col")]/a/@href').extract()[0]
			image_id = href[href.index('=')+1:len(href)]

			item['name'] 		= name
			item['category'] 	= category[category.index('=')+1:category.index('&')]	# only take category id
			item['image_urls'] 	= [url]
			item['image_name']	= ['img_' + image_id]

			str = 'img_' + image_id + '.jpg' + '|' + name + '|' + category[category.index('=')+1:category.index('&')] + '\n'

			file.write(str)

			yield item

		file.close()
	