"""
使用math库中的pi常数，计算圆的面积和体积
math库是Python的内置数学函数库，需要导入后使用
"""
# 程序：用分支判断半径r的值
import math

r = -2
if r > 0:
    area = math.pi * r * r
    print(area)
else:
    print("半径为负，请修改程序")
