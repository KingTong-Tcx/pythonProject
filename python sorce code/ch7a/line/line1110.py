 1   #program1110.py
 2   class DemoClass3:
 3       def instancemethod(self):       #成员方法
 4           print("instance method")
 5       @staticmethod
 6       def staticmethod1():            #静态方法
 7           print("static method")
 8   obj = DemoClass3()
 9   obj.instancemethod()
10   obj.staticmethod1()
11   DemoClass3.staticmethod1()
