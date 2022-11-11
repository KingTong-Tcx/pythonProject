 1   #program0308.py
 2   '''计算1！+2！+……+5!'''
 3   def factorial(n):       #计算阶乘的函数
 4       t = 1
 5       for i in range(1,n+1):
 6           t = t * i
 7       return t
 8   #计算阶乘和
 9   k = 6
10   sum1 = 0
11   for i in range(1,6):
12       sum1 += factorial(i)
13   print("1！+2！+……+5!=",sum1)
