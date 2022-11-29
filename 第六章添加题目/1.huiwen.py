# 用函数实现判断一个字符串是否为回文。比如“12321”为回文。
def huiwen(t):
    head = 0
    real = len(t) - 1
    for i in range(len(t) // 2):
        if t[head] == t[real]:
            head += 1
            real -= 1
        else:
            return False
    return True


a = input("请输入一串字符串：")
flag = huiwen(a)
if flag:
    print("yes")
else:
    print("no")
