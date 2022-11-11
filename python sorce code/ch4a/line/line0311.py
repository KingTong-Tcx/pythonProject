1  # program0311.py
2
k = eval(input("请输入计算阶乘的数值： "))
3
sum1 = 0
4
i = 1
5
while i <= k:
    6
t = j = 1
7
while j <= i:
    8
t *= j
9
j += 1
10
11
sum1 += t
12
i += 1
13
14
print(sum1)
