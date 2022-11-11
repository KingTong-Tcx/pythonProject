#program1110.py
class DemoClass3:
    def instancemethod(self):       #成员方法
        print("instance method")
    @staticmethod
    def staticmethod1():            #静态方法
        print("static method")
obj = DemoClass3()
obj.instancemethod()
obj.staticmethod1()
DemoClass3.staticmethod1()
