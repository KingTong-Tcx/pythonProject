# program0313.py
s = 0
for i in range(6):
    x = eval(input("请输入数值数据：  "))
    if x < 0: continue
    s += x

print("正数之和是： ", s)
