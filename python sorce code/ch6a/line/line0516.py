
 1   #program0516.py
 2   def fib(i):
 3       if i==0:
 4           return 0
 5       elif i==1:
 6           return 1
 7       else:
 8           return fib(i-1)+fib(i-2)
 9   
10   print(fib(8))
