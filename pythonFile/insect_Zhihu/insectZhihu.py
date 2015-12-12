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
global _user_cookie

def login_zhihu():
	zhihu_url = 'http://www.zhihu.com'
	login_url = zhihu_url+'/login/email'
	_Captcha_URL_Prefix = zhihu_url + '/captcha.gif?r='
	_Cookies_File_Name = 'cookies.json'

	login_data = {
	    'rememberme': 'true',
	}

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

	# 得到当前的时间戳 可有可无
	def gen_time_stamp():
	    return str(int(time.time())) + '%03d' % random.randint(0, 999)


	# 开始访问一次 得到post的数据 _xsrf 在cookie中
	def get_xsrf(url=None):
		html = s.get(url,headers=head)
		_cookies = html.cookies
		return _cookies.values()[3]
		# for i in range(0,len(_cookies.values())):
		# 	print "键{0}:{1} \n值:{2}\n".format(i,_cookies.keys()[i],_cookies.values()[i])
		# q_c1 = _cookies.values()[2]
		# n_c = _cookies.values()[1]
		# cap_id = _cookies.values()[0]

	_xsrf = get_xsrf(zhihu_url)
	login_data['_xsrf'] = _xsrf.encode('utf-8')
	login_data['email'] = raw_input('email: ')
	login_data['password'] = raw_input('password: ')


	# 得到验证码图片
	def save_vertifyCodeImg(imgurl):
		captcha = s.get(imgurl,stream=True)
		print captcha
		f = open('code.gif', 'wb')
		for line in captcha.iter_content(10):
			f.write(line)
		f.close()

	save_vertifyCodeImg('http://www.zhihu.com/captcha.gif?r=' + gen_time_stamp())

	# 输入验证码
	captcha = raw_input("captcha: ")
	login_data['captcha'] = captcha

	# 发送数据
	html_post = s.post(login_url,headers=head,data=login_data)
	print html_post.text

	# 保存cookie到本地
	_user_cookie = html_post.cookies
	cookieF = file("saveState.cookie","w+")
	cookieF.write("Cookie:")
	for i in range(0,len(_user_cookie.values())):
		# print "键{0}:{1} \n值:{2}\n".format(i,_cookies.keys()[i],_cookies.values()[i])
		cookieF.write(_user_cookie.keys()[i] + "=" + _user_cookie.values()[i] + ";")

	# test
	res = s.get("http://www.zhihu.com/question/29755376?sort=created", headers=head, cookies=_user_cookie)
	# print res.text

	inputF = file("insectZhihu_data.html","w+")
	inputF.write(res.text)

def startInsect():
    login_zhihu()

if __name__ == '__main__':
    startInsect()

