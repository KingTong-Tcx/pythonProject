def test1():
    # 从键盘输入一个数，判断该数是否为自然数，如果是，输出 YES
    i = eval(input("请输入一个数："))
    if i - int(i) == 0 and i > 0:
        print('YES')
    else:
        print("NO")


def test2():
    # 从键盘输入一个字符，判断它是否为小写字母，如果是则变成大写输出，否则直接输出
    i = input("请输入一个字符：")
    if 'a' <= i <= 'z':
        print(chr(ord(i) - 32))
    else:
        print(i)


def test3():
    # 从键盘输入一串字符，如果输入的全是小写字母，那转换为大写字母输出，否则不变输出
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


def test4():
    # 从键盘上输入一个自然数，判断它是否为两位数，如果是，输出YES 否则输出NO
    i = eval(input("输入一个自然数："))
    if len(str(i)) == 2 and i > 0 and i - int(i) == 0:
        print("YES")
    else:
        print("NO")


def test5():
    # 5.从键盘上输入一个整数，判断它是否为两位数，如果是，就输出YES"，否则输出。
    i = eval(input('请输入整数：'))
    if type(i) == int:
        if 9 < i < 100:
            print('YES')
        else:
            print(i)
    else:
        print('请输入整数')


def test6():
    # 6.从键盘上输入一个数，判断它的正负，是正数，则输出“+”，是负数，则输出
    i = eval(input('请输入：'))
    if i > 0:
        print('+')
    elif i < 0:
        print(i)
    else:
        print('重新输入')


def test7():
    # 7.从键盘输入一个数，求其相反数
    i = eval(input('请输入：'))
    print(0 - i)


def test8():
    # 从键盘上输入三个数，输出最大的数
    a = eval(input("输入第一个数："))
    b = eval(input("输入第二个数："))
    c = eval(input("输入第三个数："))
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    print(c)
