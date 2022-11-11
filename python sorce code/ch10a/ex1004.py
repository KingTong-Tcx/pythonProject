#program0804.py
'''
从键盘输入一个整数，求100除以它的商，并显示。
对从键盘输入的数进行异常处理,若无异常发生，打印提示信息。
'''
try:
    x=int(input("请输入数据"))
    print(100/x)
except ZeroDivisionError:
    print("异常信息：除数不能为0")
except ValueError:
    print("异常信息：输入数据必须是拉伯数字")
else:
     print("程序正常结束，未捕获到异常")
