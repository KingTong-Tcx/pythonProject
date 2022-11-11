# program0418.py
list1 = [1, 42, 3, -7, 8, 9, -10, 5]
# 二分查找要求查找的序列时有序的，假设是升序列表
list1.sort()
print(list1)

find = eval(input("请输入要查看的数据："))

low = 0
high = len(list1) - 1
flag = False
while low <= high:
    mid = int((low + high) / 2)

    if list1[mid] == find:
        flag = True
        break
    # 左半边
    elif list1[mid] > find:
        high = mid - 1
    # 右半边
    else:
        low = mid + 1

if flag == True:
    print("您查找的数据{},是第{}个元素".format(find, mid + 1))
else:
    print("没有您要查找的数据")
