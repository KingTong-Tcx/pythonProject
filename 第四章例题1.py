def test1():
    # 铁路部门规定：行李不超过50kg重的，托运费按每公斤0.15元计算，如果超过50kg，超过部分每公斤另加收0.10元。从键盘上输入行李重量，输出运费
    a = eval(input("请输入行李重量："))
    # 判断这个a是否为整数，如果是整数，如果不是整数，
    if a - int(a) != 0:
        a = int(a) + 1
    if a <= 50:
        pay = a * 0.15
    else:
        pay = 50 * 0.15 + (a - 50) * 0.25
    print("运费为：", pay)


# test1()


def test2():
    # 某超市规定，购物不足50元的按原价付款，超过50元不足100元的按9折付款，超过100元的，超过部分按8折付款，从键盘输入金额，输出付款金额
    a = eval(input("请输入金额："))
    if 50 < a <= 100:
        a = 0.9 * a
    elif a > 100:
        a = 100 * 0.9 + (a - 100) * 0.8
    print("付款金额为：", a)


# test2()


def test3():
    # 从键盘输入成绩，大于等于90，显示'优秀'；80至89，显示'良好'；70至79，显示'中等'；60至69，显示'及格'；小于60，显示'不及格'；其他显示'输入错误'
    a = eval(input("请输入成绩："))
    if 90 <= a <= 100:
        print("优秀")
    elif a >= 80:
        print("良好")
    elif a >= 70:
        print("中等")
    elif a >= 60:
        print("及格")
    elif a >= 0:
        print("不及格")
    else:
        print("输入错误")


# test3()


def test4():
    # 从键盘上输入三角形的三个边长，判断这个三角形是等腰三角形还是直角三角形
    a = eval(input("请输入三角形的第一条边长:"))
    b = eval(input("请输入三角形的第二条边长:"))
    c = eval(input("请输入三角形的第三条边长:"))
    if a + b > c and a + c > b and b + c > a:
        if a == b or b == c or a == c:
            print("等腰", end='')
        if (a ** 2 + b ** 2) - c ** 2 < 1e-5 or (b ** 2 + c ** 2) - a ** 2 < 1e-5 or (a ** 2 + b ** 2) - c ** 2 < 1e-5:
            print("直角", end='')
        print("三角形")
    else:
        print("不是三角形")


# test4()


def test5():
    # 计算100之内所有能被7整除的数之和
    sum1 = 0
    for i in range(101):
        if i % 7 == 0:
            sum1 += i
    print(sum1)


# test5()


def test6():
    # 计算1000之内所有能被7整除的数或者含有7的数之和
    sum1 = 0
    for i in range(101):
        if i % 7 == 0:

            sum1 = 0
            for i in range(1001):
                if i % 7 == 0:
                    sum1 += i
                elif "7" in str(i):
                    sum1 += i
            sum1 += i

    print(sum1)


# test6()


def test7():
    # 斐波那契数列第一个数和第二个数分别为1和1，从第三个数开始，每个数等于前两个数之和，编写一个程序输出斐波那契数列的前20个数，要求5个数一行
    a, b, c = 1, 1, 1
    print('斐波那契数列前20项为：')
    while c <= 20:
        if c % 5 == 0:
            print(a)
        else:
            print(a, end=' ')
        a, b = b, a + b
        c += 1


# test7()

def test8():
    # 从键盘输入一个正整数n，求1+2+3+。。。+n和S
    a = eval(input('请输入：'))
    sum1 = 0
    for i in range(a):
        sum1 += i
    print(sum1)


# test8()


def test9():
    # 从键盘上输入10个人的三门课的成绩，求出总分最高值并输出
    lists = [[] for _ in range(10)]
    sum1 = 0
    for i in range(10):
        sum2 = 0
        lists[i] = eval(input('请输入成绩:'))
        for a in range(0, len(lists[i])):
            sum2 = sum2 + lists[i][a]
            if sum2 > sum1:
                sum1 = sum2
    print(sum1)


# test9()


def test10():
    # 求1-3+5-7+...-99+101
    sum1 = 0
    a = 0
    for i in range(102):
        if i % 2 == 1:
            a += 1
            if a % 2 == 1:
                sum1 += i
            else:
                sum1 -= i
    print(sum1)


# test10()


def test11():
    # 从键盘输入一个正整数n,求n!
    a = eval(input('请输入：'))
    sum1 = 1
    for i in range(1, a + 1):
        sum1 = sum1 * i
    print(sum1)


# test11()


def test12():
    # 输出水仙花数，就是指三位数中的每位数的立方和还等于该数
    for i in range(100, 1000):
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        if a ** 3 + b ** 3 + c ** 3 == i:
            print(i)


test12()


def test13():
    # 求1000之内的完全数
    for i in range(1, 1000):
        sum1 = 0
        for j in range(1, i):
            if i % j == 0:
                sum1 += j
        if sum1 == i:
            print(i)


# test13()
