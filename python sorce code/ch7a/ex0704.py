# program1104.py
class Dog:

    def __init__(self, id=0, color="yellow"):  # 构造方法
        self.id = id
        self.color = color

    def show(self):
        print("id值:{} 颜色:{}".format(self.id, self.color))


dog1 = Dog()  # 构造dog1对象
dog1.show()
dog2 = Dog(101, "black")  # 构造dog2对象
dog2.show()
