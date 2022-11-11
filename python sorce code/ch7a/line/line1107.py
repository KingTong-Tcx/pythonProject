
 1   #program1107.py
 2   class Animal:
 3       num=0      #类属性
 4       def __init__(self,aname,acolor):#构造方法
 5           self.name=aname      #实例属性
 6           self.color=acolor
 7       def show(self):          #成员方法，类属性用类名访问
 8           print("名字:{},颜色：{},数量：{}".format(self.name,self.color,Animal.num))
 9   ani1 =Animal("fish","white")
10   ani2 =Animal("bird","green")
11   ani1.show()
12   ani2.show() 
13   Animal.num=2   #修改类属性的值
14   ani1.show()
15   ani2.show()    
16                 
17   
