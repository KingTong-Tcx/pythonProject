# program1107.py
class Animal:
    num = 0  # 类属性

    def __init__(self, aname, acolor):  # 构造方法
        self.name = aname  # 实例属性
        self.color = acolor

    def show(self):  # 成员方法，类属性用类名访问
        print("名字:{},颜色：{},数量：{}".format(self.name, self.color, Animal.num))


ani1 = Animal("fish", "white")
ani2 = Animal("bird", "green")
ani1.show()
ani2.show()
Animal.num = 2  # 修改类属性的值
ani1.show()
ani2.show()
