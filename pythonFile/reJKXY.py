# coding=utf-8
import requests
import sys
import re

reload(sys) 
sys.setdefaultencoding( "utf-8" )
type = sys.getfilesystemencoding()

url = 'http://news.qq.com/'

head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9     (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'}

html = requests.get(url,headers=head)
html.encoding = "gb2312"

_cookies = html.cookies
print _cookies

result = re.findall('<a target="_blank" class="linkto" href="([^<>]*?)">(.*?)<\/a>', html.text, re.S) # ?是用来分段匹配 
srcArray =  [0 for index in result]
srcIndex = 0

for each in result:
    # print "结果是:{0}和{1}\n".format(each[0],each[1])
    srcArray[srcIndex] = each[0]
    srcIndex+=1

# method 通过链接得到文本
def getHttpSrcText(url,headers,encoding):
	html = requests.get(url,headers=headers)
	html.encoding = encoding
	return html.text

###<p style="TEXT-INDENT: 2em">新华网约翰内斯堡12月3日电 （记者陈贽 邓玉山杨依军）国家主席习近平和夫人彭丽媛3日在南非约翰内斯堡出席中非合作论坛峰会欢迎宴会。</p>

articleRes = re.findall('style="TEXT-INDENT: 2em">([^<>]*?)<\/P>' ,getHttpSrcText(srcArray[0],head,'gb2312'), re.S)

for each in articleRes:
	print each

print getHttpSrcText('http://zhihu.com',head,'utf-8')

########################	分割线	#############################
result_option = re.findall('select name="Channel" id="newChannel">(.*?)<\/select>', html.text, re.S)

print result_option[0]

result_option_val = result_option[0];

all_select_obj = re.findall('option value="([^(www|00)$]*?)" >(.*?)</option>',result_option_val,re.S)

tempArray =  [0 for index in all_select_obj]

index = 0

for each in all_select_obj:
    tempArray[index] = each
    index+=1


for i in range(0, index):
	print "第{0}个{1}".format(i,tempArray[i])

htmltemp = requests.get("http://news.open.qq.com/cgi-bin/article.php?site=house&cnt=36&of=json&callback=jsonp1449234752100&_=1449235438190",headers=head)
htmltemp.encoding = "gb2312"

print htmltemp.text




