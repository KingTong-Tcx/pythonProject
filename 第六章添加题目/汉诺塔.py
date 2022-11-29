# coding:utf-8
"""
    n为初始时A柱上的盘子数
    a为起始盘子所在的柱子
    b为中转柱子
    c为目的地柱子
"""


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print("盘子从%s移动到%s" % (a, c))
        hanoi(n - 1, b, a, c)


hanoi(3, "A", "B", "C")
