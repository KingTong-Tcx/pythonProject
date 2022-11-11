#program1111.py
class Animal:
    num = 0
    def __init__(self):
        print("父类Animal")
    def show(self):
        print("父类Animal成员方法")

class Cat(Animal):
     def __init__(self):
        print("构建子类Cat")
     def run(self):
        print("子类Cat成员方法")
        
cat=Cat()
cat.run()       #子类方法
cat.show()      #父类方法
