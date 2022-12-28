# 2.设计一个Circle（圆）类，包括圆心位置、半径、颜色等属性。编写构造方法和其他方法，计算周长和面积。请编写程序验证Circle（圆）类的功能。
import math


class Circle:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def get_circlehear(self):
        return "圆心为(%s,%s)" % (self.x, self.y)

    def get_radius(self):
        return "半径为：%s" % self.r

    def get_color(self):
        return "颜色为：%s" % self.color

    def get_circumference(self):
        return "周长为：%s" % (2 * math.pi * self.r)

    def get_area(self):
        return "面积为：%s" % round((math.pi * self.r * self.r), 2)


circle = Circle(1, 2, 3.0, "红")
print(circle.get_circlehear(), circle.get_radius(), circle.get_color())
print(circle.get_circumference(), circle.get_area())
