# _*_ coding:utf-8 _*_
import http.cookiejar
import random
import time

from bson.objectid import ObjectId
from pymongo import MongoClient

from 淘宝登陆cookies import Logintaobao


url = 'https://www.taobao.com/'
client = MongoClient('10.2.1.87',27017)
db = client['save_cookie']
collection = db['taobao_cookies']


def get_cookie_lib():
    # 声明一个CookieJar对象实例来保存cookie
    cookie = http.cookiejar.LWPCookieJar()
    #调用登陆类，获取cookies {字典格式}
    user = Logintaobao('账号', '密码')
    cookie_dict = user.login()
    for cook in cookie:
        cookie_dict[cook.name] = cook.value
    return cookie_dict

def save_cookie_into_mongodb(cookie):
    insert_data = {}
    insert_data['cookie'] = str(cookie)
    insert_data['insert_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
    insert_data['request_url'] = url
    insert_data['insert_timestamp'] = time.time()
    collection.insert(insert_data)

def delete_timeout_cookie(request_url):
    #淘宝2小时cookies 过期
    time_out = 3600
    for data in collection.find({'request_url':request_url}):
        if (time.time() - data.get('insert_timestamp')) > time_out:
            print ('delete: %s' % data.get('_id'))
            collection.delete_one({'_id': ObjectId(data.get('_id'))})
#这里有疑问的话可以参考http://api.mongodb.com/python/current/tutorial.html#querying-by-objectid

def get_cookie_from_mongodb():
    #cookies = [data.get('cookie') for data in collection.find()]
    for data in collection.find({'request_url':url}):
        cookies = data.get('cookie')
        return eval(cookies)


if __name__ == '__main__':
    num=0
    while 1:
        if num == 2:
            delete_timeout_cookie(url)
            num = 0
        else:
            cookie = get_cookie_lib()
            save_cookie_into_mongodb(cookie)
            aaa = get_cookie_from_mongodb()
            num += 1
            time.sleep(random.uniform(1800,1850))

