def test0():
    # 求出10000以内所有含7的但不能被5整除且不含0的数。
    for i in range(1, 10001):
        if i % 5 != 0 and '7' in str(i) and '0' not in str(i):
            print(i)


# test0()
def test01():
    # 猴子
    y = 1
    for i in range(9, 0, -1):
        x = (y + 1) * 2
        y = x
    print(x)


# test01()

def test1():
    # 求解百钱买鸡问题。假设大鸡5元一只，中鸡3元一只，小鸡一元三只，现有100元钱想买100只鸡，有多少种买法？
    # x-大鸡 y-中鸡 z-小鸡
    for x in range(0, 21):
        for y in range(0, 34):
            z = 100 - x - y
            if z % 3 == 0:
                if (x * 5 + y * 3 + z / 3) == 100:
                    print(f"大鸡：{x}只，中鸡买：{y}只，小鸡买：{z}只")


# test1()


def test2():
    # 从键盘输入一个1到10的数，例如5，用循环实现 5*5 *
    i = eval(input("请输入一个数："))
    for x in range(i):
        print('*  ' * i)


# test2()


def test3():
    # 从键盘输入一个1到10的数，例如5，用循环实现 5*5 * 5*4 *
    i = eval(input("请输入一个数："))
    for x in range(1, i + 1):
        print('*' * x)


# test3()


def test4():
    i = eval(input("请输入一个数："))
    for x in range(i, 0, -1):
        print(x, end=' ')
        for y in range(x):
            print('*', end=' ')
        print()

# test4()
