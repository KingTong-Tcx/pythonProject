
 1   #program1111.py
 2   class Animal:
 3       num = 0
 4       def __init__(self):
 5           print("父类Animal")
 6       def show(self):
 7           print("父类Animal成员方法")
 8   
 9   class Cat(Animal):
10        def __init__(self):
11           print("构建子类Cat")
12        def run(self):
13           print("子类Cat成员方法")
14           
15   cat=Cat()
16   cat.run()       #子类方法
17   cat.show()      #父类方法
