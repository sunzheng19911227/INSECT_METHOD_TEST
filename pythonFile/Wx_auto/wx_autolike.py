# coding=utf-8
import requests
import sys
import re
import time
import random
"""
porschegt23@foxmail.com
一个登录知乎的爬虫程序

"""


reload(sys) 
sys.setdefaultencoding( "utf-8" )
type = sys.getfilesystemencoding()

def login_zhihu():
	url = 'http://mp.weixin.qq.com/mp/appmsg_like?__biz=MzA4ODE1MTc3NQ==&mid=401157557&idx=1&like=1&f=json&appmsgid=401157557&itemidx=&uin=MTI1MjAyMjgxMg%253D%253D&key=ac89cba618d2d976555e4f2262751bedd0dc5ca344c63aaa95d60bc1413f727bb4d711aec2ff1f0fad3ca73b202720d3&pass_ticket=TgL1mTdOivDdrrWy4Ct8xF1NI03Dxvh2d8v4rEaX9%25252FPn2Ju1t1Rbkk5oiPURI1uP&wxtoken=3833338203&devicetype=android-19&clientversion=26010042&x5=1';

	login_data = {
	    'rememberme': 'true',
	}

	head = {
		'Accept': 'text/xml, text/html, application/xhtml+xml, image/png, text/plain, */*;q=0.8',
        'Accept-Charset': 'utf-8, iso-8859-1, utf-16, *;q=0.7',
        'Accept-Encoding':'gzip',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
        'Q-UA2':'QV=2&PL=ADR&PR=TBS&PB=GE&VE=B1&VN=1.0.1.0002&CO=X5&COVN=025438&RF=PRI&PP=com.tencent.mm&PPVC=26010042&RL=800*1280&MO= M040 &DE=PHONE&OS=4.4.4&API=19&CHID=11111&LCID=9422',
        'X-Requested-With':'XMLHttpRequest',
        'Q-GUID':'8fedf8f66f676fb33ebb8741377988cb',
        'Q-Auth':'31045b957cf33acf31e40be2f3e71c5217597676a9729f1b',
        'Host': 'mp.weixin.qq.com',
        'Origin':'http://mp.weixin.qq.com',
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; M040 Build/KTU84P) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025438 Mobile Safari/533.1 MicroMessenger/6.1.0.66_r1062275.542 NetType/WIFI', 
        'Referer': 'http://mp.weixin.qq.com/s?__biz=MzA4ODE1MTc3NQ==&mid=401157557&idx=1&sn=971294232509b327932bd59a98c6b787&scene=4&uin=MTI1MjAyMjgxMg%3D%3D&key=ac89cba618d2d976555e4f2262751bedd0dc5ca344c63aaa95d60bc1413f727bb4d711aec2ff1f0fad3ca73b202720d3&devicetype=android-19&version=26010042&lang=zh_CN&nettype=WIFI&pass_ticket=TgL1mTdOivDdrrWy4Ct8xF1NI03Dxvh2d8v4rEaX9%2FPn2Ju1t1Rbkk5oiPURI1uP'
	}

	# 发送数据
	html_post = requests.post(url,headers=head)
	print html_post.text

def startInsect():
    login_zhihu()

if __name__ == '__main__':
    startInsect()

