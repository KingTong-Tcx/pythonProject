
 1   # program1113.py
 2   class Animal:
 3       def __init__(self,isAnimal):
 4           self.isAnimal=isAnimal
 5       def run(self):
 6           print("父类Animal通用的run()方法")
 7       def show(self):
 8           print("父类Animal的show()方法")
 9   
10   class Cat(Animal):
11       def __init__(self): 
12           print("子类的构造方法")
13       def run(self):          #方法重写
14           super().run()       #调用父类的run()方法
15           print("子类cat重写的run()方法")
16   
17   ani=Animal(False)
18   ani.show()
19   cat=Cat()     #子类的构造方法
20   cat.run()                    
21   cat.show()    #父类方法
