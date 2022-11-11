
 1   #program0517.py
 2   def factorial(i):
 3       "求指定参数的阶乘"
 4       t=1
 5       for i in range(1,i+1):
 6           t*=i
 7       return t
 8   
 9   print(factorial(6))      #720
