# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
import pymongo
from scrapy.exceptions import DropItem
import tb.settings as settings
from tb.items import MongodbItem,MongodbCommentItem


class RedisPipeline(object):
    def __init__(self):
        self.redis_db = redis.Redis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)
        self.redis_dc = settings.MY_REDIS

    def process_item(self, item, spider):
        if self.redis_db.exists(item['url']):
            raise DropItem('%s is exists!' %(item['url']))
        else:
            self.redis_db.lpush(self.redis_dc,item['url'])
        return item


class MongodbPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient('mongodb://{}:{}'.format(settings.MONGODB_HOST, settings.MONGODB_PORT))
        self.db = self.conn[settings.MONGODB_DB]
        self.dc_tb = self.db[settings.MONGODB_DC_tb_goods]
        self.dc_tb_comment = self.db[settings.MONGODB_DC_tb_goods_comment]
    def process_item(self, item, spider):
        if isinstance(item, MongodbItem):
            if self.site_goods_exist(item):
                self.dc_tb.insert(dict(item))
            else:
                raise DropItem('%s is exist!' % (item['pid']))
            return item

        if isinstance(item, MongodbCommentItem):
            if self.site_comment_exist(item):
                self.dc_tb_comment.insert(dict(item))
            else:
                raise DropItem('%s ,%s is exist!' % (item['comment'],item['pid']))
            return item

    def site_goods_exist(self,item):
        if self.dc_tb.find_one({'pid':item['pid']}):
            return False
        else:
            return True
    def site_comment_exist(self,item):
        if self.dc_tb_comment.find_one({'comment':item['comment'],'pid':item['pid']}):
            return False
        else:
            return True

