# coding=utf-8
import requests
import sys
import re
import time
import random

reload(sys) 
sys.setdefaultencoding( "utf-8" )
type = sys.getfilesystemencoding()

url = 'http://www.zhihu.com'
login_url = url+'/login/email'
_Captcha_URL_Prefix = _Zhihu_URL + '/captcha.gif?r='
_Cookies_File_Name = 'cookies.json'

head = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
        'Connection': 'keep-alive',
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36', 
        'Referer': 'http://www.zhihu.com/'
        }

s = requests.session()
def gen_time_stamp():
    return str(int(time.time())) + '%03d' % random.randint(0, 999)

_xsrf = ""

# 开始访问一次
def get_xsrf(url=None):
	html = s.get(url,headers=head)
	_cookies = html.cookies
	_xsrf = _cookies.values()[3]
	# for i in range(0,len(_cookies.values())):
	# 	print "键{0}:{1} \n值:{2}\n".format(i,_cookies.keys()[i],_cookies.values()[i])
	
	# q_c1 = _cookies.values()[2]
	# n_c = _cookies.values()[1]
	# cap_id = _cookies.values()[0]




# 验证码图片
imgURL = _Captcha_URL_Prefix + gen_time_stamp()
print imgURL
# 保存验证码图片
imgData = requests.get(imgURL,headers=head)
with open('code.gif', 'wb') as f:
    f.write(imgData.content)

# 输入验证码
captcha = raw_input("captcha: ")
print(captcha)

_email = raw_input("email: ")
_password = raw_input("password: ")

# 发送的数据
data = {'_xsrf':_xsrf, 'password':_pass, 'remember_me':'true', 'email':_email, 'captcha':captcha}
html_post = s.post(login_url,headers=head,data=data)

print html_post.text



