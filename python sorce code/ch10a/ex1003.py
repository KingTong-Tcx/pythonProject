# program0803.py
try:
    x=int(input("请输入数据"))
    print(100/x)
except ZeroDivisionError:
    print("异常信息：除数不能为0")
except ValueError:
    print("异常信息：输入数据必须是拉伯数字")
