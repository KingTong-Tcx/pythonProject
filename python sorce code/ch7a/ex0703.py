# program1103.py
class Dog:
    def __init__(self):  # 构造方法
        self.color = "black"  # 初始化对象的color属性值为"black"

    def show(self):
        print("颜色{}".format(self.color))


dog = Dog()  # 构造对象
dog.show()
