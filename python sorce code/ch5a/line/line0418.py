1  # program0418.py
2
list1 = [1, 42, 3, -7, 8, 9, -10, 5]
3  # 二分查找要求查找的序列时有序的，假设是升序列表
4
list1.sort()
5
print(list1)
6
7
find = eval(input("请输入要查看的数据："))
8
9
low = 0
10
high = len(list1) - 1
11
flag = False
12
while low <= high:
    13
mid = int((low + high) / 2)
14
15
if list1[mid] == find:
    16
flag = True
17
break
18  # 左半边
19 elif list1[mid] > find:
20
high = mid - 1
21  # 右半边
22 else:
23
low = mid + 1
24
25
if flag == True:
    26
print("您查找的数据{},是第{}个元素".format(find, mid + 1))
27 else:
28
print("没有您要查找的数据")
