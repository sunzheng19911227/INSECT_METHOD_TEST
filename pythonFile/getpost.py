# coding=utf-8
import requests
import sys
import re

reload(sys) 
sys.setdefaultencoding( "utf-8" )
type = sys.getfilesystemencoding()
url = 'https://www.crowdfunder.com/browse/deals&template=false'     

head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9     (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'}

# html = requests.get(url).text
# print html

data = {
	'entities_only':'true',
	'page':'2'
}

html_post = requests.post(url,data=data)
title = re.findall('"card-title">(.*?)<\/div>',html_post.text,re.S)

for each in title:
	print each





