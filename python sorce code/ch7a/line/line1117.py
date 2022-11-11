
 1   # program1117.py
 2   class Student:
 3       def __init__(self,name,age):
 4           self.name=name
 5           self.age=age
 6       def __str__(self):       #重载 __str__()
 7           return "{} {}".format(self.name,self.age)
 8       def __ge__(self,obj):    #重载 __ge__()
 9           if self.age>=obj.age:
10               return True
11           return False
12   
13   s1=Student("Rose",17)
14   s2=Student("John",19)
15   print("学生s1：",s1)
16   print("学生s2：",s2)
17   print("学生大小的比较：",s1>=s2)
18   
19   
