1  # program0313.py
2
s = 0
3
for i in range(6):
    4
x = eval(input("请输入数值数据：  "))
5
if x < 0: continue
6
s += x
7
8
print("正数之和是： ", s)
