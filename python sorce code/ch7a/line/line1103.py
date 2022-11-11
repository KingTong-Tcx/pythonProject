1   #program1103.py
2   class Dog:
3       def __init__(self):       #构造方法
4           self.color="black"     #初始化对象的color属性值为"black"
5       def show(self):            
6           print("颜色{}".format(self.color))
7   
8   dog =Dog()             #构造对象
9   dog.show()
10   
11   
