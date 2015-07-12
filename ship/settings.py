# -*- coding: utf-8 -*-

# Scrapy settings for ship project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ship'

SPIDER_MODULES = ['ship.spiders']
NEWSPIDER_MODULE = 'ship.spiders'
DOWNLOAD_DELAY = 0.75

# ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
ITEM_PIPELINES = {'ship.pipelines.ShipImagesPipeline': 1}
IMAGES_STORE = 'train'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ship (+http://www.yourdomain.com)'
