1   # program0101.py
2   # 输入三角形三条边，有海伦公式计算三角形面积s。
3   import math
4   a=eval(input("请输入a边长："))
5   b=eval(input("请输入b边长："))
6   c=eval(input("请输入c边长："))
7   p = (a + b + c) / 2
8   s = math.sqrt(p * (p - a) * (p - b) * (p - c))
9   print("三角形的面积是{:.2f}".format(s))
