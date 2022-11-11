
 1   #program1115.py
 2   class Animal:
 3       def __init__(self,aname):
 4           self.name=aname
 5       def enjoy(self):
 6           print("nangnang")
 7   
 8   class Cat(Animal):
 9       def enjoy(self):
10           print(self.name," niaoniao")
11   
12   class Dog(Animal):
13       def enjoy(self):
14           print(self.name+" wangwang")
15           
16   class Person:
17       def __init__(self,id,name):
18           self.name=name
19           self.id=id
20       def drive(self,ani):
21           ani.enjoy()
22              
23   cat=Cat("Mikey")
24   dog=Dog("Dahuang")
25   person=Person("zhang3",9)
26   person.drive(cat)
27   person.drive(dog)
28   
29   
