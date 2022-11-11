1  # program0316.py
2
num = [];
3
i = 2
4
for i in range(2, 100):
    5
j = 2
6
for j in range(2, i):
    7
if (i % j == 0):
    8
break
9 else:
10
num.append(i)
11
print(num)
