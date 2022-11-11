1   #program1101.py
2   class Dog:
3       num = 0              #类属性
4       def __init__(self,id=0,color="yellow"):#构造方法
5           self.id=id
6           self.color=color
7           
8       def enjoy(self):     #成员方法
9           print("wangwang")
10   dog =Dog()
11   dog.enjoy()
12   
