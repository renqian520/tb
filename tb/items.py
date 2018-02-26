# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RedisItem(scrapy.Item):
    url = scrapy.Field()

class MongodbItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    pid = scrapy.Field()
    shuxing = scrapy.Field()
    sale_count = scrapy.Field() #月销量
    #xid = scrapy.Field()  #作为店铺的唯一标识   <a href="//zhaoshang.tmall.com/maintaininfo/liangzhao.htm?xid=f577537d109f2e3b85f43543ac733828"

class MongodbCommentItem(scrapy.Item):
    pid = scrapy.Field()
    comment = scrapy.Field()
    pubtime = scrapy.Field()