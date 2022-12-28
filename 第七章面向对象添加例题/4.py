# 设计一个Person类，属性有姓名、年龄、性别，创建方法personInfo，打印输出这个人的信息；
# 创建Student类，继承Person类，属性有学院college，班级Group，重写父类PersonInfo方法，
# 调用父类方法打印输出个人信息，将学生的学院、班级信息也打印输出出来。

class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def personInfo(self):
        return "姓名为：%s 年龄为：%s 性别：%s " % (self.name, self.age, self.sex)


class Student(Person):
    def __init__(self, name, age, sex, college, group):
        Person.__init__(self, name, age, sex)
        self.college = college
        self.group = group

    def personInfo(self):
        return super().personInfo() + "学院:%s 班级:%s" % (self.college, self.group)


per = Student("abc", 22, "男", 123, 321)
print(per.personInfo())
