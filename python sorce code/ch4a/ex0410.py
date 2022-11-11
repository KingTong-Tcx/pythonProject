# program0312.py
a = eval(input("请输入的数值："))
i = a // 2  # 等价于i=int(a/2)
while i > 0:
    if a % i == 0: break
    i -= 1
print(a, "的最大真约数为：", i)
