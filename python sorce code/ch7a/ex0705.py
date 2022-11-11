# program1105.py
class Dog:
    def __init__(self):  # 构造方法
        self.color = "black"

    def show(self):
        print("颜色:{},id:{}".format(self.color, self.id))

    def __del__(self):
        print("对象被清除")


dog = Dog()
dog.id = 1
dog.show()
# del dog
