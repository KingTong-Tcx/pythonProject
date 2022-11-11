'''已知学生类Student，成员变量有id(序号)，name(姓名)，course(课程,String)。
学生类的集合类StuList，承载多学生信息。
实现学生信息追加，修改，删除，排序等操作。
'''
class Student:
    def __init__(self,id,name,course):
        self.id=id
        self.name=name
        self.course=course

    def __str__(self):
        return "{} {} {}".format(self.id,self.name,self.course)

class StuList:
    #datas=[]
    def __init__(self,data):
        self.data=data[:]

    def __getitem__(self,index):
        return self.data[index]
    def __setitem__(self,index,value):
        self.data[index]=value   

    def __delitem__(self,index):
        del self.data[index]
        
##以下主控程序
s1=Student(12,"Rose","Python")
s2=Student(4,"John","Java")
s3=Student(7,"Allen","CSS")
lst=[s1,s2,s3]
stulist=StuList(lst)
print("------遍历原始数据--------")
for item in stulist:
    print(item)
    
print("-----追加数据后遍历-------")
s4=Student(102,"Feng","Algorithm")
stulist.data.append(s4)
for item in stulist:
    print(item)
    
print("------修改数据后遍历------")
s5=Student(208,"张林","Algorithm")
stulist[2]=s5
for item in stulist:
    print(item)
    
print("--------排序后遍历--------")
stulist.data.sort(key=lambda x:x.id,reverse=False)
for item in stulist:
    print(item)
    
print("--------删除后遍历--------")
del(stulist[2])    
for item in stulist:
    print(item)

    
