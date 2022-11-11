
 1   # program1119.py
 2   '''已知学生类Student，成员变量有id(序号)，name(姓名)，course(课程)。
 3   学生类的集合类StuList，承载多名学生信息。
 4   实现学生信息追加，修改，删除，排序等操作。
 5   '''
 6   class Student:
 7       def __init__(self,id,name,course):
 8           self.id=id
 9           self.name=name
10           self.course=course
11       def __str__(self):
12           return "{} {} {}".format(self.id,self.name,self.course)
13   
14   class StuList:
15       def __init__(self,data):
16           self.data=data[:]
17       def __getitem__(self,index):
18           return self.data[index]
19       def __setitem__(self,index,value):
20           self.data[index]=value   
21       def __delitem__(self,index):
22           del self.data[index]
23           
24   ##以下主控程序
25   s1=Student(12,"Rose","Python")
26   s2=Student(4,"John","Java")
27   s3=Student(7,"Allen","CSS")
28   lst=[s1,s2,s3]
29   stulist=StuList(lst)
30   print("------遍历原始数据--------")
31   for item in stulist:
32       print(item)
33   print("------追加数据后遍历------")
34   s4=Student(102,"Feng","Algorithm")
35   stulist.data.append(s4)
36   for item in stulist:
37       print(item)
38   print("------修改数据后遍历------")
39   s5=Student(208,"张林","Algorithm")
40   stulist[2]=s5
41   for item in stulist:
42       print(item)
43   print("--------排序后遍历--------")
44   stulist.data.sort(key=lambda x:x.id,reverse=False)
45   for item in stulist:
46       print(item)
47   print("--------删除后遍历--------")
48   del(stulist[2])    
49   for item in stulist:
50       print(item)
