# -*- coding: utf-8 -*-

# Scrapy settings for tb project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import random
import datetime
BOT_NAME = 'tb'

SPIDER_MODULES = ['tb.spiders']
NEWSPIDER_MODULE = 'tb.spiders'

#第一种输出每日日志监控，异常维护  scrapy runspider  ***.py时 启用
# LOG_ENABLED = True
# LOG_FILE = datetime.datetime.now().strftime('%Y-%m-%d') +'-jd.log'
# LOG_LEVEL = 'DEBUG'

#第二种输出每日日志监控，异常维护
# curl http://localhost:6800/schedule.json -d project=项目名 -d spider=爬虫名
#查看对应的logs文件

# 使用了scrapy-redis里的去重组件，不使用scrapy默认的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用了scrapy-redis里的调度器组件，不实用scrapy默认的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 使用队列形式
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 允许暂停，redis请求记录不丢失
SCHEDULER_PERSIST = False

#宽度优先，质量更高
SCHEDULER_ORDER = 'BFO'

#mongodb
MONGODB_URI = 'mongodb://10.2.1.87:27017/'
MONGODB_HOST = "10.2.1.87"
MONGODB_PORT = 27017
MONGODB_DB = "tb"
MONGODB_DC_tb_goods = "ec_tb_goods"
MONGODB_DC_tb_goods_comment = "ec_tb_goods_comment"

#redis
REDIS_HOST = "10.2.1.87"
REDIS_PORT = 6379
REDIS_DB = 0
MY_REDIS = 'tb_spider:start_urls' #redis数据表
#设置爬虫运行时间，如果爬虫还没有结束，则自动关闭
CLOSESPIDER_TIMEOUT = 82800

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tb (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#CONCURRENT_ITEMS = 100
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = random.uniform(0.3,3)
RANDOMIZE_DOWNLOAD_DELAY = True
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tb.middlewares.TbSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware' : None,
    'tb.useragent.UserAgent':50,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 90,
     'tb.middlewares.ProxyMiddleware':100,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #'jd.pipelines.JdPipeline': 500,
    'scrapy_redis.pipelines.RedisPipeline':300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
