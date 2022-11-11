
 1   # program1116.py
 2   class Computing:
 3       '''列表与数字的加减操作'''   
 4       def __init__(self,value):
 5           self.value = value
 6       def __add__(self,other):
 7           lst=[]
 8           for i in self.value:
 9               lst.append(i+other)
10           return lst  
11       def __sub__(self,other):
12           lst=[]
13           for i in self.value:
14               lst.append(i-other)
15           return lst
16   
17   c = Computing([-1,3,4,5])
18   print("+运算符重载后的列表",c+2)     #+运算符重载
19   print("+运算符重载后的列表",c-2)     #-运算符重载
