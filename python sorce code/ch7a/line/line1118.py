
 1   # program1117.py
 2   class SelectData:
 3       def __init__(self,data):
 4           self.data=data[:]
 5       def __getitem__(self,index):
 6           return self.data[index]
 7       def __setitem__(self,index,value):
 8           self.data[index]=value
 9       def __delitem__(self,index):
10           del self.data[index]
11   
12   x=SelectData([12,33,23,"ab",False])
13   print(x)        #x的地址
14   print(x[:])     #x中的全部元素
15   print(x[2])     #x中的第2个元素
16   print(x[2:])    #x中从第2个起的全部元素
17   x[4]=100        #替换x中的第4个元素
18   print(x[:])
19   del(x[3])       #删除x中的第3个元素
20   for num in x:   #遍历对象x中的元素
21       print(num,end=" ")
