1  # program0312.py
2
a = eval(input("请输入的数值："))
3
i = a // 2  # 等价于i=int(a/2)
4
while i > 0:
    5
if a % i == 0: break
6
i -= 1
7
print(a, "的最大真约数为：", i)
