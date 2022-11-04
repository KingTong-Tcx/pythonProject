# ex0407.py
lst = [1, 3, 7, -23, 34, 0, 23, 2, 9, 7, 79]

head = 0
tail = len(lst) - 1
# while head < len(lst) / 2:
#     lst[head], lst[tail] = lst[tail], lst[head]
#     head += 1
#     tail -= 1
# for item in lst:
#     print(item, end="   ")
for head in range(0,int((len(lst))/2)):
    lst[head], lst[tail] = lst[tail], lst[head]
    tail -= 1
for item in lst:
    print(item, end="   ")