 1   #program1102.py
 2   class Dog:
 3       num = 0              #类属性 
 4       def __init__(self,id=0,color="yellow"):#构造方法
 5           self.id=id
 6           self.color=color
 7       def enjoy(self):     #成员方法
 8           print("wangwang")
 9       def show(self,weight):
10           print("重量{}公斤".format(weight))
11           print("颜色{}".format(self.color))
12   dog =Dog(color="grey")
13   dog.weight=52
14   dog.show(dog.weight)
15   dog.enjoy()
