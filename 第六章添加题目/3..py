# 将列表 ls = [23,45,78,87,11,67,89,13,243,56,67,311,431,111,141]中的素数去除，并输出去除素数后列表ls 的元素个数。
ls = [23, 45, 78, 87, 11, 67, 89, 13, 243, 56, 67, 311, 431, 111, 141]
temp = []
for i in ls:
    flag = True
    for j in range(2, i // 2):
        if i % j == 0:
            flag = False
            break
    if flag:
        temp.append(i)

for i in temp:
    ls.remove(i)
print(len(ls))
for i in ls:
    print(i, end=" ")
print()
print("----------------------------------------------------------------------")
# 将列表 ls = [23,45,78,87,11,67,89,13,243,56,67,311,431,111,141]中的素数保留，并输出保留素数后列表ls 的元素个数。
ls = [23, 45, 78, 87, 11, 67, 89, 13, 243, 56, 67, 311, 431, 111, 141]
temp = []
for i in ls:
    flag = True
    for j in range(2, i // 2):
        if i % j == 0:
            flag = False
            break
    if not flag:
        temp.append(i)

for i in temp:
    ls.remove(i)
print(len(ls))
for i in ls:
    print(i, end=" ")

