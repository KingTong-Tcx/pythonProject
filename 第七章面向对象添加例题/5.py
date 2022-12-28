# 5.定义一个交通工具(Vehicle)的类，属性：速度(speed)、体积(size)等等。方法：移动move()、设置速度setSpeed(int speed)、加速speedUp()、减速speedDown()等等。
# 实例化一个交通工具对象，通过方法初始化speed、size的值并且在相关方法中可以打印输出出来；另外调用加速减速的方法对速度进行改变。

class Vehicle:
    def __init__(self, speed, size, time, acceleration):
        self.speed = speed
        self.size = size
        self.time = time
        self.acceleration = acceleration

    def move(self):
        return "初速度：{} 加速度：{} 体积：{}".format(self.speed, self.acceleration, self.size)

    def setSpeed(self, speed):
        self.speed = speed
        return "设置的初速度是：{}".format(self.speed)

    def speedUp(self):
        speed_end_up = self.speed + self.acceleration * self.time
        return "加速完后速度是：{}".format(speed_end_up)

    def speedDown(self):
        speed_end_down = self.speed - self.acceleration * self.time
        if speed_end_down < 0:
            return "减完速后速度是：0"
        else:
            return "减完速后速度是：{}".format(speed_end_down)

car = Vehicle(1, 2, 5, 2)
print(car.move())
print(car.setSpeed(100))
print(car.speedUp())
print(car.speedDown())
