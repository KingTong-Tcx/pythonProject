1   # program0105.py
2   '''
3   输入三角形三条边，有海伦公式计算三角形面积s。
4   在对三边进行了异常处理基础上，判断3边符合三角形条件。
5   '''
6   import math
7   try:
8       a=eval(input("请输入a边长："))
9       b=eval(input("请输入b边长："))
10       c=eval(input("请输入c边长："))
11   except NameError:
12       print("请输入正数数值")
13   if a<0 or b<0 or c<0:
14       print("输入数据不可以为负数")
15   elif a+b<=c or a+c<=b or b+c<=a:
16        print("不符合两边之和大于第三边原则")
17   else:   
18       p = (a + b + c) / 2
19       s = math.sqrt(p * (p - a) * (p - b) * (p - c))
20       print("三角形的面积是{:.2f}".format(s))
 
