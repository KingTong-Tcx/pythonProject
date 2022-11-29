# 计算杨辉三角 定义法
n = eval(input("输入要打印的行数："))
triangle = [[1], [1, 1]]
for i in range(2, n):  # 已经给出前两行，求剩余行
    pre = triangle[i-1]  # 上一行
    cul = [1]  # 定义每行第一个元素
    for j in range(i-1):  # 算几次
        cul.append(pre[j]+pre[j+1])  # 每个数字等于上一行的左右两个数字之和。
    cul.append(1)  # 添加每行最后一个元素
    triangle.append(cul)
print("普通输出:{}".format(triangle))
for i in range(n):  # 按等边三角形格式输出
    s = " "*(n-i-1)
    for j in triangle[i]:
        s = s + str(j)+" "
    print(s)
