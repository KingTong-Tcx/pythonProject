# program1113.py
class Animal:
    def __init__(self,isAnimal):
        self.isAnimal=isAnimal
    def run(self):
        print("父类Animal通用的run()方法")
    def show(self):
        print("父类Animal的show()方法")

class Cat(Animal):
    def __init__(self): 
        print("子类的构造方法")
    def run(self):          #方法重写
        super().run()       #调用父类的run()方法
        print("子类cat重写的run()方法")

ani=Animal(False)
ani.show()
cat=Cat()     #子类的构造方法
cat.run()                    
cat.show()    #父类方法
