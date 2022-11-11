
 1   #program1112.py
 2   class Employee:
 3       def __init__(self,name="",department="computer",age=20):
 4           self.setName(name)
 5           self.setDepartment(department)
 6           self.setAge(age)
 7       def setName(self,name):
 8           if type(name)!=str:
 9               print("姓名必须是字符")
10               return
11           self.__name=name
12       def setDepartment(self,department):
13           if department not in ["computer","communication","electric"]:
14               print("专业必须是computer、communication或electric")
15               return
16           self.__department=department
17       def setAge(self,age):
18           if type(age)!=int or age>=33 or age<20:
19               print("年龄必须是数字，且界于20至33之间")
20               return
21           self.__age=age
22       def show(self):
23           print("姓名：{} 专业：{} 年龄：{}".
24                 format(self.__name,self.__department,self.__age))
25   
26   class ProjectManager(Employee):
27       def __init__(self,name='',department="computer",age=22,title="middle"):
28           Employee.__init__(self,name,department,age)
29           self.setTitle(title)
30       def setTitle(self,title):
31           self.__title=title
32       def show(self):
33           Employee.show(self)
34           print("职称：{}".format(self.__title))
35           
36   try:
37       emp1=Employee("Rose")
38       emp1.show()
39       pm1=ProjectManager("Mike","electric",26,"high")
40       pm1.setAge(30)
41       pm1.show()
42   except Exception as ex:
43       print("数据出现错误",ex)
44   
