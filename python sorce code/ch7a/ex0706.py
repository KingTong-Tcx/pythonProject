# program1106.py
class Animal:
    '''
    类中未定义构造方法，使用默认的构造方法
    def __init__(self):
        self.color=color
    '''
    num = 0  # 类属性

    # enjoy()方法没有self参数，普通的方法，由类名调用
    def enjoy():
        print("wangwang")

    # show()方法使用self参数，成员方法
    def show(self, args):
        print("重量{}公斤".format(args))


ani = Animal()
ani.weight = 52
Animal.enjoy()  # ani.enjoy()错误
ani.show(ani.weight)
