# coding=utf-8
import requests
import sys
import re
import time

reload(sys) 
sys.setdefaultencoding( "utf-8" )
type = sys.getfilesystemencoding()

_Zhihu_URL = 'http://www.zhihu.com'
_Login_URL = _Zhihu_URL + '/login'
_Captcha_URL_Prefix = _Zhihu_URL + '/captcha.gif?r='
_Cookies_File_Name = 'cookies.json'

head = {'X-Requested-With': 'XMLHttpRequest',
       'Referer': 'http://www.zhihu.com',
       'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; '
                     'Trident/7.0; Touch; LCJB; rv:11.0)'
                     ' like Gecko',
       'Host': 'www.zhihu.com'}

html = requests.get(_Zhihu_URL,headers=head)
html.encoding = "gb2312"

_cookies = html.cookies

for i in range(0,len(_cookies.values())):
	print "键{0}:{1} \n值:{2}\n".format(i,_cookies.keys()[i],_cookies.values()[i])

_xsrf = _cookies.values()[3]
q_c1 = _cookies.values()[2]
n_c = _cookies.values()[1]
cap_id = _cookies.values()[0]

# 验证码图片
imgURL = _Captcha_URL_Prefix + str(int(time.time() * 1000))
print imgURL
# 保存验证码图片
imgData = requests.get(imgURL,headers=head)
with open('code.gif', 'wb') as f:
        f.write(imgData.content)

# f = file("code.gif","w+")
# f.write(imgData.text)
# f.close()

# 发送的数据
#	_xsrf:8f677ad0d6da9a563a0331e8b7a527e7
#	password:TingGT2911Long
#	captcha:fzyd
#	remember_me:true
#	email:531365872%40qq.com
data = {'_xsrf':_xsrf, 'password':'TingGT2911Long', 'remember_me':'true', 'email':'531365872@qq.com'}


# print _cookies.keys()
# print _cookies.values()

# _cookies.save('cookiefile.txt')


