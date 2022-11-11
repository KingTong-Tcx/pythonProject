# program0309.py
lst = [1, 3, 7, -23, 34, 0, 23, 2, 9, 7, 79]

head = 0
tail = len(lst) - 1
while head < len(lst) / 2:
    lst[head], lst[tail] = lst[tail], lst[head]  # 头尾互换
    head += 1  # 调整头指针后移
    tail -= 1  # 调整尾指针前移

for item in lst:
    print(item, end="  ")
