# tb

淘宝商品详情+评论爬虫+天猫工商执照（Scrapy、Redis）

基于Python+scrapy+redis+mongodb的分布式爬虫实现框架

scrapy runspider tbredisurl.py 主要功能是抓取种子url，保存到redis

scrapy runspider tbmongodb.py 主要是从redis里面读url，解析数据保存到mongodb （拓展到其他机器,修改REDIS_HOST = "主机ip"，都是从redis里面读url,MONGODB_HOST = "存储服务器ip"）

middlewares.ProxyMiddleware 使用阿布云代理服务器轮换请求IP

淘宝登陆cookies.py 主要功能是模拟登陆淘宝，拿到cookies

taobaocookies.py 主要功能是将cookies池定时维护存储在mongodb中，淘宝cookies有效期大约在1-2小时，需要进行及时更新，每隔半小时执行一次。

yumdama.py 第三方云打码平台，解决验证码验证。

淘宝工商执照.py 主要功能是将天猫店铺工商执照页面，经过验证码识别后的图片下载下来，并进行base64解码，使用pytesseract进行图片识别。

使用Spiderkeeper监控爬虫管理，定期执行，分析日志报告，异常维护。


                                                    淘宝商品信息mongodb图示
![淘宝商品信息](https://github.com/renqian520/tb/blob/master/%E6%B7%98%E5%AE%9D%E5%95%86%E5%93%81%E4%BF%A1%E6%81%AF.jpg)

                                                    淘宝商品评论mongodb图示
![淘宝商品评论](https://github.com/renqian520/tb/blob/master/%E6%B7%98%E5%AE%9D%E5%95%86%E5%93%81%E8%AF%84%E8%AE%BA.jpg)

                                                    天猫店铺工商执照mongodb图示
![天猫店铺工商执照](https://github.com/renqian520/tb/blob/master/%E5%A4%A9%E7%8C%AB%E5%BA%97%E9%93%BA%E5%B7%A5%E5%95%86%E6%89%A7%E7%85%A7%E4%BF%A1%E6%81%AF.jpg)
