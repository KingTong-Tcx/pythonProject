# 用函数实现求100-200里面所有的素数。
def qiushushu(t1, t2):
    lst = []
    for i in range(t1, t2 + 1):
        flag = True
        for j in range(2, i//2):
            if i % j == 0:
                flag = False
                break
        if flag:
            lst.append(i)
    return lst


lst1 = qiushushu(100, 200)
print(len(lst1))
for i in range(len(lst1)):
    print(lst1[i], end=" ")
