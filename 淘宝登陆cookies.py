import requests

class Logintaobao():
    def __init__(self,name,pwd):
        self.username = name
        self.password = pwd
        self.session = requests.Session()

    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/603.2.5 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.5",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 Mobile/14F89 Safari/602.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/58.0.3029.110 Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.2.5 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36 OPR/46.0.2597.32",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/59.0.3071.109 Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.898",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.39",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
        ]
    def login(self):
        loginURL = 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
        ua = '106#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'

        password2 = '210b8a1500855a666aa2a3e2c4be0c5985ffbd2cef3c8715e766bab7909cfb07b8a04acbbc8b63578e04fe0eedd57053dee7e3708e9d33107b3b4720ec00a97639aaedc087c0fa2722b2a8e573f96e6047a386502d9ceeb7e20b6d8af6af2e1eda66bc3c93aa667ec75416a505fe599ec9d432c8811981b308903284796917fa'

        postData = {
        'TPL_username': self.username,
        'TPL_password': '',
        'ncoSig': '',
        'ncoSessionid': '',
        'ncoToken': '0902a5bc81ddf6962402a38749418c9c1d39dd79',
        'slideCodeShow': 'false',
        'useMobile':'false',
        'lang': 'zh_CN',
        'loginsite': '0',
        'newlogin': '0',
        'TPL_redirect_url': 'https://www.taobao.com/',
        'from': 'tb',
        'fc': 'default',
        'style': 'default',
        'css_style': '',
        'keyLogin': 'false',
        'qrLogin': 'true',
        'newMini': 'false',
        'newMini2': 'false',
        'tid': '',
        'loginType': '3',
        'minititle': '',
        'minipara': '',
        'pstrong': '',
        'sign': '',
        'need_sign': '',
        'isIgnore': '',
        'full_redirect': '',
        'sub_jump': '',
        'popid': '',
        'callback': '',
        'guf': '',
        'not_duplite_str': '',
        'need_user_id': '',
        'poy': '',
        'gvfdcname': '10',
        'gvfdcre': '',
        'from_encoding': '',
        'sub': '',
        'TPL_password_2': password2,
        'loginASR': '1',
        'loginASRSuc': '1',
        'allp': '',
        'oslanguage': 'zh-CN',
        'sr': '1920*1080',
        'osVer': '',
        'naviVer': 'chrome|63.03239132',
        'miserHardInfo': '',
        'ua': ua,
        'um_token': 'HV01PAAZ0b8720ac73ec2d8e5a55c9f8001ea377'
        }
        headers = {
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9',
            'origin': 'https://login.taobao.com',
            'referer': 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F',
            'connection': 'Keep-Alive',
            'upgrade-insecure-requests':'1',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

        }
        req = self.session.post(loginURL,postData,headers=headers)
        #cookies = self.session.cookies.get_dict()
        print(self.session.cookies.get_dict())
        #mm = self.session.get('https://member1.taobao.com/member/fresh/deliver_address.htm?spm=a1z02.1.a210b.8.113555anOUNQR')
        #print(mm.text)
        return self.session.cookies.get_dict()

if __name__ == '__main__':
    aa = Logintaobao('账号','密码')
    aa.login()




