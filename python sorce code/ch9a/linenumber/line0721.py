1  # program0721.py
2
from datetime import date, datetime

3
import pickle

4
5


def savedata():


    6
'''
7       使用字典保存模块名称，创建时间和模块功能等信息，
8       使用列表保存多个模块信息。
9       '''
10
modules = []
11
m1 = {"name": "登录注册", "描述": '使用字典保存模块名称，创建时间和模块功能信息'}
12
m2 = {"name": "订单管理", "日期": date(2017, 10, 12),
      "描述": '订单管理模块实现的是订单数据的输入、追加、修改和删除等功能'}
13
m3 = {"name": "客户管理", "日期": datetime.now(), "描述": '使用字典保存模块名称，创建时间和模块功能信息'}
14
15
modules.append(m1)
16
modules.append(m2)
17
modules.append(m3)
18
19
file = open("minfo.data", "ab")
20
pickle.dump(modules, file)
21
file.close()
22
print("数据写入成功\n")
23
24
file = open("minfo.data", "rb")
25
lst1 = pickle.load(file)
26
for item in lst1:
    27
print(item)
28
file.close()
29
print("\n数据读取结束")
30
31
savedata()  # 调用函数数
