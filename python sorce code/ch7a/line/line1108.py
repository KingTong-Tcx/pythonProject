 1   #program1108.py
 2   class DemoClass1:
 3       def instancemethod(self):      #实列方法
 4           print("instance method")
 5       @classmethod          
 6       def classmethod1(cls):         #类方法
 7           print("class method")
 8   obj = DemoClass1()
 9   obj.instancemethod()
10   obj.classmethod1()
11   DemoClass1.classmethod1()
