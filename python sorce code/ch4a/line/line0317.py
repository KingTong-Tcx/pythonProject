1  # program0317.py
2
import random

3
NUMBER = 100000
4
n = 0
5
for i in range(NUMBER):
    6
x = random.random() * 2 - 1
7
y = random.random() * 2 - 1
8
if ((x * x + y * y) <= 1):
    9
n += 1
10
pi = 4.0 * n / NUMBER
11
print("使用蒙特卡罗方法计算圆周率的值是：", pi)
