
 1   #program0521.py
 2   basis=100            #全局变量
 3   def func3(x,y):
 4       basis=90         #与全局变量同名，但是局部变量，与全局变量无关
 5       sum=basis+x+y
 6       return sum
 7   
 8   print("{:6.2f}".format(func3(75,62)))
 9   print(basis)         #全局变量值仍为100
10   print("------------------------")
