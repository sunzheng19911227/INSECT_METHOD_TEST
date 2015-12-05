# coding=utf-8
a = 10
b = 2
c = a + b
print c

if c <= 12 :
    print "正确"
elif c > 12 :
    print "错误"
else :
    print "离谱"

for i in range(0,5):
    print "items {0},{1}".format(i,"hello")

def sayHello():
    print "sayHello"

sayHello()

def max(a,b):
    if a > b:
        return a
    else :
        return b

print "最大值是{0}".format(max(2,3))





