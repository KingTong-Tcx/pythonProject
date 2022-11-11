
 1   #program0523.py
 2   basis=100            #全局变量
 3   def func4(x,y):
 4       global basis     #声明basis是函数外的全局变量
 5       print(basis)     #100
 6       basis=90
 7       sum=basis+x+y
 8       return sum
 9   
10   print(func4(75,62))
11   print(basis)          #90
