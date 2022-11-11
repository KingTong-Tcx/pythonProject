
 1   # program1106.py
 2   class Animal:
 3       '''
 4       类中未定义构造方法，使用默认的构造方法
 5       def __init__(self):
 6           self.color=color
 7       '''
 8       num = 0              #类属性
 9       # enjoy()方法没有self参数，普通的方法，由类名调用
10       def enjoy():     
11           print("wangwang")
12       # show()方法使用self参数，成员方法
13       def show(self,args):
14           print("重量{}公斤".format(args))
15   ani =Animal()
16   ani.weight=52
17   Animal.enjoy()    #ani.enjoy()错误
18   ani.show(ani.weight)
19   
20                 
21                 
22   
