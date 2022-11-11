#program0317.py
import random
NUMBER = 100000
n = 0
for i in range(NUMBER):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    if ((x * x + y * y) <= 1):
        n+=1
pi = 4.0 * n / NUMBER
print("使用蒙特卡罗方法计算圆周率的值是：",pi)
