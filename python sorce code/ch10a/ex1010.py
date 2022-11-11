# program0810.py
'''输入两个数，计算两数之间的所有质数'''
try:
    x = int(input("请输入第1个数:"))
    y = int(input("请输入第2个数:"))
    assert x > 2 and y > 2, "x和y必须为大于2的正整数"
    if x > y:
        x, y = y, x
    num = []
    i = x
    for i in range(x, y + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            num.append(i)
    print("{}和{}之间的质数为{}".format(x, y, num))
except Exception as result:
    print("异常信息：", result)
