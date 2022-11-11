
 1   # program1120.py
 2   class DataList:
 3       '''All the elements in this array must be numbers'''
 4     
 5       def __isNumber(self, n):
 6           if not isinstance(n, (int, float, complex)):
 7               return False
 8           return True
 9   
10       def __init__(self, *args):
11           if not args:
12               self.__data = []
13           else:
14               for arg in args:
15                   if not self.__isNumber(arg):
16                       print('All elements must be numbers')
17                       return
18               self.__data = list(args)
19   
20       #重载运算符+
21       #列表中每个元素都与数字n相加，或两个列表相加，返回新列表
22       def __add__(self, n):
23           temp=DataList()
24           if self.__isNumber(n):
25              temp.__data = [item+n for item in self.__data]
26              return temp
27           elif isinstance(n, DataList):
28               temp.__data = [i+j for i, j in zip(self.__data, n.__data)]        
29               return temp
30           else:
31               print('Not supported')
32   
33       #重载运算符-
34       ##列表中每个元素都与数字n相减，返回新列表
35       def __sub__(self, n):
36           if not self.__isNumber(n):
37               print('- operating with {},Datatype Error'.format(type(n)))
38               return
39           temp=DataList()
40           temp.__data = [item-n for item in self.__data]
41           return temp
42   
43       #重载运算符*
44       #列表中每个元素都与数字n相乘，返回新列表
45       def __mul__(self, n):
46           if not self.__isNumber(n):
47               print('* operating with {},Datatype Error'.format(type(n)))
48           return
49           temp=DataList()
50           temp.__data = [item*n for item in self.__data]
51           return temp
52   
53       #重载运算符/
54       #列表中每个元素都与数字n相除，返回新列表
55       def __truediv__(self, n):
56           if not self.__isNumber(n):
57               print('/ operating with {},Datatype Error'.format(type(n)))
58               return
59           temp=DataList()
60           temp.__data = [item/n for item in self.__data]
61           return temp
62   
63       #重载运算符%
64       #列表中每个元素都与数字n求余数，返回新列表
65       def __mod__(self, n):
66           if not self.__isNumber(n):
67               print( print('% operating with {},Datatype Error'.format(type(n))))
68               return
69           temp=DataList()
70           temp.__data = [item%n for item in self.__data]
71           return temp
72   
73       def __len__(self):        
74           return len(self.__data)
75   
76       #直接使用该类对象作为表达式来查看对象的值
77       def __repr__(self):
78           return repr(self.__data)
79   
80       #支持使用print()函数查看对象的值
81   ##    def __str__(self):
82   ##        return str(self.__data)
83   
84       #追加元素
85       def append(self, value):
86           if not self.__isNumber(value):
87               print('Only number can be appended.')
88               return
89           self.__data.append(value)
90   
91       #获取指定下标的元素值，支持使用列表或元组指定多个下标
92       def __getitem__(self, index): 
93           length = len(self.__data)
94           #如果指定单个整数作为下标，则直接返回元素值
95           if isinstance(index, int) and 0<=index<length: 
96               return self.__data[index]
97           #使用列表或元组指定多个整数下标
98           elif isinstance(index, (list,tuple)):
99               for i in index:
100                   if not (isinstance(i,int) and 0<=i<length):
101                       return 'index error'
102               result = []
103               for item in index:
104                   result.append(self.__data[item])
105               return result
106           else:
107               return 'index error'
108   
109       #修改元素值，支持使用列表或元组指定多个下标，同时修改多个元素值
110       def __setitem__(self, index, value):
111           length = len(self.__data)
112           #如果下标合法，则直接修改元素值
113           if isinstance(index, int) and 0<=index<length:
114               self.__data[index] = value
115           #支持使用列表或元组指定多个下标
116           elif isinstance(index, (list,tuple)):
117               for i in index:
118                   if not (isinstance(i,int) and 0<=i<length):
119                       raise Exception('index error')
120               #如果下标和给的值都是列表或元组，并且个数一样，则分别为多个下标的元素修改值
121               if isinstance(value, (list,tuple)):
122                   if len(index) == len(value):
123                       for i, v in enumerate(index):
124                           self.__data[v] = value[i]
125                   else:
126                       raise Exception('values and index must be of the same length')
127               #如果指定多个下标和一个普通值，则把多个元素修改为相同的值
128               elif isinstance(value, (int,float,complex)):
129                   for i in index:
130                       self.__data[i] = value
131               else:
132                   raise Exception('value error')
133           else:
134               raise Exception('index error')
135   
136       #支持成员测试运算符in，测试列表中是否包含某个元素
137       def __contains__(self, value):        
138           if value in self.__data:
139               return True
140           return False
141   
142       #重载运算符==，测试两个列表是否相等
143       def __eq__(self, value):
144           if not isinstance(value, DataList):
145               print(value, ' must be an instance of DataList.')
146               return False
147           if self.__data == value.__data:
148               return True
149           return False
150   
151       #重载运算符<，比较两个列表大小
152       def __lt__(self, value):
153           if not isinstance(value, DataList):
154               print(v, ' must be an instance of DataList.')
155               return False
156           if self.__data < value.__data:
157               return True
158           return False
159       
160   ## 主控程序
161   if __name__ == '__main__':
162       x=DataList(1,3,5,7,9)
163       y=DataList(-2,-4,-8)
164       print(x)
165       print("x+y=",x+y)
166       print("x==y=",x==y)
167       print("x+2=",x+2)
168       print("x%2=",x%2)
169       print("5 in x=",5 in x)
170       print("x<y=",x<y)
171       x[4]=['a','b','c']
172       print(x)
173       x[2,4,1]=True
174       print(x)
