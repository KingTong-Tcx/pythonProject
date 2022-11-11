
 1   #program0522.py
 2   basis=100            #全局变量
 3   def func4(x,y):
 4       print(basis)
 5       basis=90
 6       sum=basis+x+y
 7       return sum
 8   
 9   print(func4(78,62))
10   print(basis)
