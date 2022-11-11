# program1116.py
class Computing:
    '''列表与数字的加减操作'''   
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        lst=[]
        for i in self.value:
            lst.append(i+other)
        return lst  
    def __sub__(self,other):
        lst=[]
        for i in self.value:
            lst.append(i-other)
        return lst

c = Computing([-1,3,4,5])
print("+运算符重载后的列表",c+2)     #+运算符重载
print("+运算符重载后的列表",c-2)     #-运算符重载
