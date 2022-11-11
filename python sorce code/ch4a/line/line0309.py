1  # program0309.py
2
lst = [1, 3, 7, -23, 34, 0, 23, 2, 9, 7, 79]
3
4
head = 0
5
tail = len(lst) - 1
6
while head < len(lst) / 2:
    7
lst[head], lst[tail] = lst[tail], lst[head]  # 头尾互换
8
head += 1  # 调整头指针后移
9
tail -= 1  # 调整尾指针前移
10
11
for item in lst:
    12
print(item, end="  ")
