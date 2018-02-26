# -*- coding: utf-8 -*-
import scrapy
from tb.items import RedisItem
import urllib.request
import time
import random


class Ecspider(scrapy.Spider):
    name = 'tbspider'
    allowed_domains = ['taobao.com']
    custom_settings = {
        'ITEM_PIPELINES':{
            'tb.pipelines.RedisPipeline':300,
        }
    }
    start_urls = []
    for keywords in open('/root/renqian/scrapy_redis/jd/jd/spiders/keywords.txt', encoding='utf-8'):
        keyword = urllib.request.quote(keywords).replace('\n','')
        for i in range(50):
            start_urls.append('https://s.taobao.com/search?q={}&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s={}'.format(str(keyword),str(i*44)))


    def parse(self, response):
        time.sleep(random.uniform(0.5,3))
        item = RedisItem()
        item['url'] = response.url
        yield item

