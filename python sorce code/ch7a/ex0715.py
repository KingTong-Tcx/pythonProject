#program1115.py
class Animal:
    def __init__(self,aname):
        self.name=aname
    def enjoy(self):
        print("nangnang")

class Cat(Animal):
    def enjoy(self):
        print(self.name," niaoniao")

class Dog(Animal):
    def enjoy(self):
        print(self.name+" wangwang")
        
class Person:
    def __init__(self,id,name):
        self.name=name
        self.id=id
    def drive(self,ani):
        ani.enjoy()
           
cat=Cat("Mikey")
dog=Dog("Dahuang")
person=Person("zhang3",9)
person.drive(cat)
person.drive(dog)


