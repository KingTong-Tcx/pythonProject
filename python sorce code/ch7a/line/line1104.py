1   #program1104.py
2   class Dog:
3   
4       def __init__(self,id=0,color="yellow"):#构造方法
5           self.id=id
6           self.color=color
7       def show(self):            
8           print("id值:{} 颜色:{}".format(self.id,self.color))
9   
10   dog1 =Dog()             #构造dog1对象
11   dog1.show()
12   dog2 =Dog(101,"black")             #构造dog2对象
13   dog2.show()
14   
15   
