1    # program0104.py
2    '''
3    输入三角形三条边，有海伦公式计算三角形面积s。
4     对三边进行了异常处理。
5   '''
6    import math
7    try:
8       a=eval(input("请输入a边长："))
9       b=eval(input("请输入b边长："))
10       c=eval(input("请输入c边长："))
11       p = (a + b + c) / 2
12       s = math.sqrt(p * (p - a) * (p - b) * (p - c))
13       print("三角形的面积是{:.2f}".format(s))
14   except NameError:
15       print("请输入正数数值")
