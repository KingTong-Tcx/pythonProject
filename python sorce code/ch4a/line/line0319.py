1  # program0319.py
2
n = eval(input("请输入打印的行数： "))
3
for x in range(1, n + 1):
    4
print(' ' * (10 - x), end="")
5
n = x
6
while n >= 1:
    7
print(n, sep="", end="")
8
n -= 1
9
10
n = 2
11
while n <= x:
    12
print(n, sep="", end="")
13
n += 1
14
print()
