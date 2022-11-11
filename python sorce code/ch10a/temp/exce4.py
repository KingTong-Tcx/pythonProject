class AgeException(Exception):
    def __init__(self, description):
        self.description = description


class Students:
    def __init__(self, strname, age):
        self.strname = strname
        self.age = age
        if (age < 0 or age > 200):
            raise AgeException("年龄错误")
        else:
            print(age)


try:
    s1 = Students("zh3", 19)
    s2 = Students("Lisi", -20)
except AgeException as e:
    print(e.description)
