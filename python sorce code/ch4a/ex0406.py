# program0308.py
'''计算1！+2！+……+5!'''


def factorial(n):  # 计算阶乘的函数
    t = 1
    for i in range(1, n + 1):
        t = t * i
    return t


# 计算阶乘和
k = 6
sum1 = 0
for i in range(1, 6):
    sum1 += factorial(i)
print("1！+2！+……+5!=", sum1)
