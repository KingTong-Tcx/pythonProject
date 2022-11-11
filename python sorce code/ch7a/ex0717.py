# program1117.py
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # 重载 __str__()
        return "{} {}".format(self.name, self.age)

    def __ge__(self, obj):  # 重载 __ge__()
        if self.age >= obj.age:
            return True
        return False


s1 = Student("Rose", 17)
s2 = Student("John", 19)
print("学生s1：", s1)
print("学生s2：", s2)
print("学生大小的比较：", s1 >= s2)
