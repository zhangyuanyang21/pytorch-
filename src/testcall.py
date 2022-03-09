class person:
    def __call__(self, name):
        print("__call__" + "hello" + name)
    def hello(self,name):
        print("hello" + name)
p = person()
p("zhangsan")
p.__call__("wangwu")
p.hello("lisi")
