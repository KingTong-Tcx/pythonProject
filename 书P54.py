# 编程题

def test1():
    # 1、给定某个字符串s，对其中的每一字符c进行大小写转换：如果c是大写字母，则将它转换成小写字母，如果c是小写字母，则将它转换成大写字母，如果不是字母，则不进行转换
    st_r = input("输入字符串！")
    a = []
    for i in range(len(st_r)):
        if 'a' <= st_r[i] <= 'z':
            a.append(st_r[i].upper())
        elif 'A' <= st_r[i] <= 'Z':
            a.append(st_r[i].lower())
        else:
            a.append(st_r[i])
    print(''.join(a))


# test1()

def test2():
    # 2、输入一个整数，将各位数字反转后输出
    a = input("请输入一个整数：")
    print(a[::-1])


# test2()
def test3():
    # 3、计算1**2-2**2+3**2-4**2+。。。+97**2-98**2+99**2。
    result = sum([((-1) ** (x - 1)) * (x ** 2) for x in range(1, 100)])
    print(result)


# test3()
def test4():
    global sum
    # 4、一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如，6的因子为1、2、3，而6=1+2+3，因此6就是"完数"。请编程找出100内的所有完数
    # 循环输出1到100之间的数  range():含头不含尾
    for i in range(1, 101):
        # 此时i代表1-100之间所有的数
        # 定义和的初始值
        sum = 0
        # 构造数字的因子
        for j in range(1, i):
            #     因子:能被i整除的是i的因子
            if i % j == 0:
                #     只要是i的因子那么就相加
                sum += j
        # 如果 因子相加的和  等于i本身那么这个数就是完数
        if sum == i:
            print(f"{i}是完数")


# test4()
def test5():
    # 5、输入两个正整数m和n，求其最大公约数和最小公倍数
    m = m1 = eval(input('请输入第一个正整数：'))
    n = n1 = eval(input('请输入第二个正整数：'))
    if m1 >= n1:  # 判断m和n哪个为较大的数
        while n1 != 0:  # 较小的数为0时，返回的大数即为最大公约数
            a = m1 % n1
            m1 = n1  # 将小数作为下一轮循环的大数
            n1 = a  # 将大数除于小数得到的的余数作为下一轮循环的小数
        u = (m * n) // m1  # 最小公倍数为两数之积除以最大公约数
        print('最大公约数%d\n最小公倍数%d' % (m1, u))
    else:
        while m1 != 0:
            a = n1 % m1
            n1 = m1
            m1 = a
        u = (m * n) // n1
        print('最大公约数%d\n最小公倍数%d' % (n1, u))


# test5()

# 6、输入一元二次方程的3个系数a、b、c，求ax^2+bx+c=0方程的根
