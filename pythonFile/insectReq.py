# coding=utf-8
import requests
import sys
import re

reload(sys) 
sys.setdefaultencoding( "utf-8" )
type = sys.getfilesystemencoding()
     
head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9     (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'}
        
html = requests.get('http://jp.tingroom.com/yuedu/yd300p/')
html.encoding = 'utf-8'

#print html.text 
title = re.findall('color:#666666;">(.*?)<\/span>', html.text, re.S) # ?是用来分段匹配 

for each in title:
        print each
