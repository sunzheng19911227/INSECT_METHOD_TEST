class Hello:
    def sayHello(self):
        print "Hello Python {0}".format(self._name)

    def __init__(self,name):
        self._name = name

class Hi(Hello):
    def __init__(self,name):
        Hello.__init__(self,name)

    def sayHi(self):
        print "Hi Python {0}".format(self._name)

#h = Hello("chang")
#h.sayHello()

#hi = Hi("zhang san")
#hi.sayHi()



