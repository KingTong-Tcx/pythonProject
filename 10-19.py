# 从键盘输入一个数，判断该数是否为自然数，如果是，输出'YES’
def test1():
    i = eval(input("请输入一个数："))
    if i - int(i) == 0 and i > 0:
        print('YES')
    else:
        print("NO")


# 从键盘输入一个字符，判断它是否为小写字母，如果是则变成大写输出，否则直接输出
def test2():
    i = input("请输入一个字符：")
    if 'a' <= i <= 'z':
        print(chr(ord(i) - 32))
    else:
        print(i)


# 从键盘输入一串字符，如果输入的全是小写字母，那转换为大写字母输出，否则不变输出
def test3():
    flag = 0
    str1 = ''
    a = input("请输入一串字符串：")
    for i in a:
        if 'a' <= i <= 'z':
            str1 = str1 + chr(ord(i) - 32)
        else:
            flag = 1
            break
    if flag == 0:
        print(str1)
    else:
        print(a)
