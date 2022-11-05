def test1():
    i = eval(input("请输入一个数："))
    for x in range(i):
        for y in range(i - 1 - x):
            print(' ', end=' ')
        for y in range(x + 1):
            print('*', end=' ')
        print()


# test1()


def test2():
    a = eval(input("请输入一个数："))
    for i in range(1, a + 1):
        print((a - i) * ' ', (2 * i - 1) * '*')


# test2()

def test3():
    a = eval(input("请输入一个数："))
    for i in range(a + 1, 0, -1):
        print((a - i + 1) * ' ', (2 * i - 1) * '*')


# test3()


def test4():
    a = eval(input("请输入一个数："))
    for i in range(1, a + 1):
        print((a - i + 1) * ' ', (2 * i - 1) * '*')
    for i in range(a + 1, 0, -1):
        print((a - i + 1) * ' ', (2 * i - 1) * '*')


# test4()

# a = eval(input("请输入一个数："))
# for i in range(a + 1, 0, -1):
#     print()

def test5():
    s = 0
    for i in range(6):
        x = eval(input("请输入数值的数据："))
        if x < 0:
            continue
        s += x
    print("正数之和是：", s)


# test5()

def test6():
    num1 = 1000
    while 1 == 1:
        if num1 % 13 == 0 and num1 % 17 == 0:
            break
        num1 += 1
    print(num1)


# test6()

def test7():
    s = 0
    for i in range(1, 11):
        s += int(i * '9')
    print(s)


# test7()
