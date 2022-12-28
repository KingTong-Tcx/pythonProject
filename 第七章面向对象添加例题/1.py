# 1.有下面的类属性：姓名、年龄、成绩列表[语文，数学，英语]，其中每门课成绩的类型为整数，类的方法如下所述：
# (1)列表项列表项获取学生的姓名。get_name()，返回类型：str。
# (2)获取学生的年龄。get_age()，返回类型：int。
# (3)返回3门科目中最高的分数。get_course()， 返回类型：int。

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.score)

    def get_course1(self):
        max1 = 0
        for i in self.score:
            max1 = self.score
        return max1

    def get_course2(self):
        max1 = 0
        for i in range(len(self.score)):
            if self.score[i] > max1:
                max1 = self.score
        return max1


zm = Student('zhangsan', 20, [69, 88, 100])

print(zm.get_name())
print(zm.get_age())
print(zm.get_course())
