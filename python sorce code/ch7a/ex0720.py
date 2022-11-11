# program1120.py
class DataList:
    '''All the elements in this array must be numbers'''
  
    def __isNumber(self, n):
        if not isinstance(n, (int, float, complex)):
            return False
        return True

    def __init__(self, *args):
        if not args:
            self.__data = []
        else:
            for arg in args:
                if not self.__isNumber(arg):
                    print('All elements must be numbers')
                    return
            self.__data = list(args)

    #重载运算符+
    #列表中每个元素都与数字n相加，或两个列表相加，返回新列表
    def __add__(self, n):
        temp=DataList()
        if self.__isNumber(n):
           temp.__data = [item+n for item in self.__data]
           return temp
        elif isinstance(n, DataList):
            temp.__data = [i+j for i, j in zip(self.__data, n.__data)]        
            return temp
        else:
            print('Not supported')

    #重载运算符-
    ##列表中每个元素都与数字n相减，返回新列表
    def __sub__(self, n):
        if not self.__isNumber(n):
            print('- operating with {},Datatype Error'.format(type(n)))
            return
        temp=DataList()
        temp.__data = [item-n for item in self.__data]
        return temp

    #重载运算符*
    #列表中每个元素都与数字n相乘，返回新列表
    def __mul__(self, n):
        if not self.__isNumber(n):
            print('* operating with {},Datatype Error'.format(type(n)))
        return
        temp=DataList()
        temp.__data = [item*n for item in self.__data]
        return temp

    #重载运算符/
    #列表中每个元素都与数字n相除，返回新列表
    def __truediv__(self, n):
        if not self.__isNumber(n):
            print('/ operating with {},Datatype Error'.format(type(n)))
            return
        temp=DataList()
        temp.__data = [item/n for item in self.__data]
        return temp

    #重载运算符%
    #列表中每个元素都与数字n求余数，返回新列表
    def __mod__(self, n):
        if not self.__isNumber(n):
            print( print('% operating with {},Datatype Error'.format(type(n))))
            return
        temp=DataList()
        temp.__data = [item%n for item in self.__data]
        return temp

    def __len__(self):        
        return len(self.__data)

    #直接使用该类对象作为表达式来查看对象的值
    def __repr__(self):
        return repr(self.__data)

    #追加元素
    def append(self, value):
        if not self.__isNumber(value):
            print('Only number can be appended.')
            return
        self.__data.append(value)

    #获取指定下标的元素值，支持使用列表或元组指定多个下标
    def __getitem__(self, index): 
        length = len(self.__data)
        #如果指定单个整数作为下标，则直接返回元素值
        if isinstance(index, int) and 0<=index<length: 
            return self.__data[index]
        #使用列表或元组指定多个整数下标
        elif isinstance(index, (list,tuple)):
            for i in index:
                if not (isinstance(i,int) and 0<=i<length):
                    return 'index error'
            result = []
            for item in index:
                result.append(self.__data[item])
            return result
        else:
            return 'index error'

    #修改元素值，支持使用列表或元组指定多个下标，同时修改多个元素值
    def __setitem__(self, index, value):
        length = len(self.__data)
        #如果下标合法，则直接修改元素值
        if isinstance(index, int) and 0<=index<length:
            self.__data[index] = value
        #支持使用列表或元组指定多个下标
        elif isinstance(index, (list,tuple)):
            for i in index:
                if not (isinstance(i,int) and 0<=i<length):
                    raise Exception('index error')
            #如果下标和给的值都是列表或元组，并且个数一样，则分别为多个下标的元素修改值
            if isinstance(value, (list,tuple)):
                if len(index) == len(value):
                    for i, v in enumerate(index):
                        self.__data[v] = value[i]
                else:
                    raise Exception('values and index must be of the same length')
            #如果指定多个下标和一个普通值，则把多个元素修改为相同的值
            elif isinstance(value, (int,float,complex)):
                for i in index:
                    self.__data[i] = value
            else:
                raise Exception('value error')
        else:
            raise Exception('index error')

    #支持成员测试运算符in，测试列表中是否包含某个元素
    def __contains__(self, value):        
        if value in self.__data:
            return True
        return False

    #重载运算符==，测试两个列表是否相等
    def __eq__(self, value):
        if not isinstance(value, DataList):
            print(value, ' must be an instance of DataList.')
            return False
        if self.__data == value.__data:
            return True
        return False

    #重载运算符<，比较两个列表大小
    def __lt__(self, value):
        if not isinstance(value, DataList):
            print(v, ' must be an instance of DataList.')
            return False
        if self.__data < value.__data:
            return True
        return False
    
## 主控程序
if __name__ == '__main__':
    x=DataList(1,3,5,7,9)
    y=DataList(-2,-4,-8)
    print(x)
    print("x+y=",x+y)
    print("x==y=",x==y)
    print("x+2=",x+2)
    print("x%2=",x%2)
    print("5 in x=",5 in x)
    print("x<y=",x<y)
    x[4]=['a','b','c']
    print(x)
    x[2,4,1]=True
    print(x)
