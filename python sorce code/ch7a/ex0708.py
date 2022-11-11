#program1108.py
class DemoClass1:
    def instancemethod(self):      #实列方法
        print("instance method")
    @classmethod          
    def classmethod1(cls):         #类方法
        print("class method")
obj = DemoClass1()
obj.instancemethod()
obj.classmethod1()
DemoClass1.classmethod1()
