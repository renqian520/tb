# _*_ coding:utf-8 _*_
# cookies 2小时左右过期
import taobaocookies
import requests
import time
import random
from PIL import Image
import base64
import pytesseract
import re
from pymongo import MongoClient
from yumdama import identify # 验证码打码平台识别

aa =taobaocookies.get_cookie_from_mongodb()

def ab(xid):

        url = 'https://zhaoshang.tmall.com/maintaininfo/liangzhao.htm?xid={}'.format(str(xid))
        headers = {
             'Host':'zhaoshang.tmall.com',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding':'gzip, deflate',
            'Referer': 'https://semir.tmall.com/shop/view_shop.htm?',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
                }
        m = requests.get(url,headers=headers,
                         cookies = aa)



        yz = re.compile('id="J_CheckCode" src="(.*?)" />').findall(m.text)
        token = re.compile("type='hidden' value='(.*?)'>").findall(m.text)


        for i,j in zip(yz,token):
            #重点  验证url 需要去掉amp;，否则会重新刷新验证码
            yz_url = 'https:'+str(i).replace('amp;','')
            print(yz_url)
            _tb_token_ = j
            header = {
            'Host': 'pin.aliyun.com',
            'Accept': 'image/png,image/*;q=0.8,*/*;q=0.5',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'https://zhaoshang.tmall.com/maintaininfo/liangzhao.htm?&xid={}'.format(str(xid)),
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
            result = requests.get(yz_url,
                              headers=header,
                                  cookies= aa)

            with open('yzm.jpg', 'wb') as f:
                f.write(result.content)
            im = Image.open('D:\\任谦\python3\\python3整理目录\\PycharmProjects\\untitled4\\yzm.jpg')
            im.show()
            im.close()
            yzm = identify() # 验证码打码平台识别
            time.sleep(random.uniform(1,4))
            out_url = 'https://zhaoshang.tmall.com/maintaininfo/liangzhao.htm?_tb_token_={}&checkCode={}&xid={}'.format(str(_tb_token_),str(yzm),str(xid))
            print(out_url)
            hd = {
                'Host':'zhaoshang.tmall.com',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                #重点，漏了就一直循环验证码
                'Referer': 'https://zhaoshang.tmall.com/maintaininfo/liangzhao.htm?_tb_token_={}&checkCode=&xid={}'.format(str(_tb_token_),str(xid)),
                'Connection': 'Keep-Alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
            }

            out = requests.get(out_url,headers=hd,
                               cookies = aa)

            aaa = re.compile('src="data:image/png;base64,(.*?)" height=',re.S).findall(out.text)

            for i in aaa:
                return i

            if '看不清' in out.text:
                return ab(xid)


if __name__ == '__main__':
    try:
        #连接mongodb  存放店铺工商执照信息
        client = MongoClient('mongodb://127.0.0.1:27017/')
        db = client.taobao
        taobao_zhizhao = db.zhizhao
        #图片的base64编码
        try:
            for x in open('D:\\任谦\\python3\\python3整理目录\\PycharmProjects\\untitled4\\xid.txt', encoding='utf-8'):
                xid = str(x).replace('\n','')
                ydm  = ab(xid)
                try:
                    img = base64.b64decode(ydm)
                    file = open('D:\\任谦\\python3\\python3整理目录\\PycharmProjects\\untitled4\\cookies密码登陆访问\\1.png', 'wb')
                    file.write(img)
                    # 图片RGBA转RGB
                    img = Image.open('D:\\任谦\\python3\\python3整理目录\\PycharmProjects\\untitled4\\cookies密码登陆访问\\1.png')
                    bg = Image.new("RGB", img.size, (255, 255, 255))
                    bg.paste(img, img)
                    #图片文字识别
                    text = pytesseract.image_to_string(bg, lang='chi_sim')  # 设置为中文文字的识别
                    with open('D:\\任谦\\python3\\python3整理目录\\PycharmProjects\\untitled4\\cookies密码登陆访问\\tupian.txt','w',encoding='utf-8') as file:
                        file.write(('xid:'+xid +'\n' + text))

                    f = open('D:\\任谦\\python3\\python3整理目录\\PycharmProjects\\untitled4\\cookies密码登陆访问\\tupian.txt',encoding='utf-8')
                    lines = f.readlines()
                    if len(lines) < 35:
                        list = []
                        for n in lines:
                            print(n)
                            list.append(n.replace('\n', '').replace(' ', '').replace('“', ''))
                        print(list)
                        xid = re.compile("xid:(.*?)',").findall(str(list))[0]
                        try:
                            a = str(re.compile("注册号(.*?)', ''").findall(str(list))[0]).replace(':', '')
                        except:
                            a = 'NULL'
                        try:
                            b = str(re.compile("名称(.*?)', ''").findall(str(list))[0]).replace(':', '')
                        except:
                            b = 'NULL'
                        try:
                            c = str(re.compile("类型(.*?)', ''").findall(str(list))[0]).replace(':', '')
                        except:
                            c = 'NULL'
                        try:
                            d = str(re.compile("住所(.*?)', ''").findall(str(list))[0]).replace(':', '')
                        except:
                            d = 'NULL'
                        try:
                            e = str(re.compile("代表人(.*?)', ''").findall(str(list))[0]).replace(':', '')
                        except:
                            e = 'NULL'
                        try:
                            f = str(re.compile("成立时间(.*?)', ''").findall(str(list))[0]).replace(':', '')
                        except:
                            f = 'NULL'
                        try:
                            g = str(re.compile("资本(.*?)', ''").findall(str(list))[0]).replace(':', '')
                        except:
                            g = 'NULL'
                        try:
                            h = str(re.compile("期限(.*?)', ''").findall(str(list))[0]).replace(':', '')
                        except:
                            h = 'NULL'
                        try:
                            i = str(re.compile("范围(.*?)', ''").findall(str(list))[0]).replace(':', '').replace("', '",
                                                                                                               '')
                        except:
                            i = 'NULL'
                        try:
                            j = str(re.compile("机关(.*?)', ''").findall(str(list))[0]).replace(':', '')
                        except:
                            j = 'NULL'
                        try:
                            k = str(re.compile("核准时间(.*?)'").findall(str(list))[0]).replace(':', '')
                        except:
                            k = 'NULL'

                        mmm = [{
                            'xid': xid,
                            "企业注册号": a,
                            "企业名称": b,
                            "类型": c,
                            "住所": d,
                            "法定代表人": e,
                            "成立时间": f,
                            "注册资本": g,
                            "营业期限": h,
                            "经营范围": i,
                            "登记机关": j,
                            "核准时间": k
                        }]
                        print(mmm)
                        taobao_zhizhao.insert(mmm)

                    else:
                        xxid = lines[0].replace('xid:', '').replace('\n', '')
                        aa = lines[1].replace(' ', '').replace('企业注册号:', '').replace('\n', '')
                        bb = lines[5].replace(' ', '').replace('\n', '')
                        cc = lines[7].replace(' ', '').replace('类“型:', '').replace('\n', '')
                        dd = lines[8].replace(' ', '').replace('住“所:', '').replace('\n', '')
                        ee = lines[9].replace(' ', '').replace('法定代表人:', '').replace('\n', '')
                        ff = lines[20].replace(' ', '').replace('\n', '')
                        gg = lines[22].replace(' ', '').replace('\n', '')
                        hh = lines[24].replace(' ', '').replace('\n', '')
                        ii = str(lines[26:-4]).replace('\\n', '').replace(' ', '').replace('[','').replace(']','').replace(",''","").replace("'",'')
                        jj = str(lines[-3:-1]).replace('\\n', '').replace(' ', '').replace('[','').replace(']','').replace(",''","").replace("'",'')
                        kk = str(lines[-1]).replace(' ', '').replace('\\n', '')
                        mmm = [{
                            'xid': xxid,
                            "企业注册号": aa,
                            "企业名称": bb,
                            "类型": cc,
                            "住所": dd,
                            "法定代表人": ee,
                            "成立时间": ff,
                            "注册资本": gg,
                            "营业期限": hh,
                            "经营范围": str(ii).replace("', '", ''),
                            "登记机关": jj,
                            "核准时间": kk
                        }]
                        print(mmm)
                        taobao_zhizhao.insert(mmm)
                except:
                    pass
        except:
            pass
    except:
        pass

