
 1   #program0517.py
 2   def factorial(i):
 3       if i==0:
 4           return 1
 5       else:
 6           return i*factorial(i-1)
 7   
 8   print(factorial(6))
