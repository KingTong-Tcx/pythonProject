 
 1   #program1105.py
 2   class Dog:
 3       def __init__(self):#构造方法
 4           self.color="black"
 5       def show(self):
 6           print("颜色:{},id:{}".format(self.color,self.id))
 7       def __del__(self):
 8           print("对象被清除")
 9   dog =Dog()
10   dog.id=1
11   dog.show()
12   #del dog
13                 
14                 
15   
