# 封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩；求总分，平均分，以及打印输出学生的相关信息。

class Student:
    def __init__(self, name, age, sex, score):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score

    def get_name(self):
        return "姓名为：%s" % self.name

    def get_age(self):
        return self.age

    def get_sex(self):
        return self.sex

    def get_course(self):
        return max(self.score)

    def get_sum(self):
        return sum(self.score)

    def get_avg(self):
        return round(sum(self.score) / 3, 2)


zm = Student('zhangsan', 20, '男', [69, 88, 100])
print(zm.get_name())
print(zm.get_age())
print(zm.get_sum())
print(zm.get_avg())
