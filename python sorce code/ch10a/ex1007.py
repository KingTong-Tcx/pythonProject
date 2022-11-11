# program0807.py
x = [12, 3, -4]
try:
    x[0] = int(input("请输入第1个数:"))
    x[1] = int(input("请输入第2个数:"))
    print(x[0] / x[1])
except Exception as result:
    print("程序出现异常", result)
