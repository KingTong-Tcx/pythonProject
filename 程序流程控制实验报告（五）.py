def test1():
    # 求10+20+30+。。。+n,当结果中出现10个0时n为几？
    n = 0
    sum1 = 0
    while 1:
        n = n + 10
        sum1 = sum1 + n
        count = 0
        k = sum1
        while k > 0:
            if k % 10 == 0:
                count += 1
            k = k // 10
        if count >= 10:
            break
    print("n为:", n)


# test1()
def test2():
    # 求10+20+30+。。。+n,当结果中出现连续3个0时n为几？
    n = 0
    sum1 = 0
    flag = 1
    while flag:
        n = n + 10
        sum1 = sum1 + n
        k = sum1
        while k > 0:
            if k % 1000 == 0:
                flag = 0
                break
            k = k // 10
    print("n为:", n)


# test2()

def test3():
    a = eval(input("请输入一个数："))
    for i in range(1, a + 1):
        for j in range(1, a + 1):
            # print("%-3d" % (i * j), end=' ')
            print("{:<3}".format(i * j), end=' ')
        print()


# test3()
# a = eval(input("请输入一个数："))
# x = 0
# for i in range(a):
#     for j in range(a):
#         x += 1
#         print("{:<3}".format(x), end=' ')
#     print()


# a = eval(input("请输入一个数："))
# for i in range(a):
#     for j in range(1, a + 1):
#         if i % 2 == 0:
#             print("{:<3}".format(i * a + j), end=' ')
#         else:
#             print("{:<3}".format((i+1)*a-j+1), end=' ')
#     print()


def test4():
    a = eval(input("请输入一个数："))
    for i in range(1, a + 1):
        for j in range(i):
            print("{:<3}".format(i), end=' ')
        print()


# test4()

def test5():
    a = eval(input("请输入一个数："))
    for i in range(1, a + 1):
        for j in range(1, i + 1):
            print("{:<3}".format(j), end=' ')
        print()


# test5()

def test6():
    a = eval(input("请输入一个数："))
    for i in range(1, a + 1):
        for j in range(i, 0, -1):
            print("{:<3}".format(j), end=' ')
        print()


# test6()

def test7():
    x = 0
    a = eval(input("请输入一个数："))
    for i in range(1, a + 1):
        for j in range(1, i + 1):
            x += 1
            print("{:<3}".format(x), end=' ')
        print()


# test7()

def test8():
    a = eval(input("请输入一个数："))
    count = 0
    for i in range(1, a + 1):
        if i % 2 == 1:
            for j in range(i, 0, -1):
                count += 1
                print("%-3d" % count, end=' ')
        else:
            count = count + i + 1
            for j in range(i, 0, -1):
                count -= 1
                print("%-3d" % count, end=' ')
            count += i - 1
        print()


# test8()

def test9():
    a = eval(input("请输入一个数："))
    for i in range(1, a + 1):
        print(' ' * (a - i), end='')
        for j in range(1, 2 * i):
            print(i, end='')
        print()


# test9()

def test10():
    a = eval(input("请输入一个数："))
    for i in range(1, a + 1):
        print(' ' * (a - i), end='')
        for j in range(1, i + 1):
            print(j, end='')
        for j in range(i - 1, 0, -1):
            print(j, end='')
        print()


# test10()


def test11():
    # p52
    a = eval(input("请输入一个数："))
    for i in range(1, a + 1):
        for j in range(a - i):
            print(" ", end=" ")
        count = i
        for j in range(1, 2 * i):
            if j < i:
                print(count, end=" ")
                count -= 1
            else:
                print(count, end=" ")
                count += 1
        print()


# test11()
def test12():
    # 九九乘法表
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{i}x{j}={i * j}\t', end='')
        print()


# test12()

def test13():
    a = eval(input("请输入一个数："))
    for i in range(1, a + 1):
        for j in range(1, a + 1):
            if i > j:
                print(i, end=' ')
            else:
                print(j, end=' ')
        print()


test13()
