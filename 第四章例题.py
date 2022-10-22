def test1():
    # 从键盘上输入一个自然数，判断它是否为两位数，如果是，输出YES 否则输出NO
    n = eval(input("输入一个自然数："))
    if len(str(n)) == 2 and n > 0 and n - int(n) == 0:
        print("YES")
    else:
        print("NO")


# test1()

def test2():
    # 从键盘上输入三个数，按从小到大顺序输出
    a = eval(input("输入第一个数："))
    b = eval(input("输入第二个数："))
    c = eval(input("输入第三个数："))
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    print(a, "   ", b, "    ", c)


# test2()

def test3():
    # 铁路部门规定：行李不超过50kg重的，托运费按每公斤0.15元计算，如果超过50kg，超过部分每公斤另加收0.10元。从键盘上输入行李重量，输出运费
    a = eval(input("请输入行李重量："))
    # 判断这个a是否为整数，如果是整数，如果不是整数，？
    if a - int(a) != 0:
        a = int(a) + 1
    if a <= 50:
        pay = a * 0.15
    else:
        pay = 50 * 0.15 + (a - 50) * 0.25
    print("运费为：", pay)


# test3()

def test4():
    # 某超市规定，购物不足50元的按原价付款，超过50元不足100元的按9折付款，超过100元的，超过部分按8折付款，从键盘输入金额，输出付款金额
    a = eval(input("请输入金额："))
    if 50 < a <= 100:
        a = 0.9 * a
    elif a > 100:
        a = 100 * 0.9 + (a - 100) * 0.8
    print("付款金额为：", a)


# test4()

def test5():
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


# test5()

def test6():
    a = eval(input("请输入三角形的第一条边长:"))
    b = eval(input("请输入三角形的第二条边长:"))
    c = eval(input("请输入三角形的第三条边长:"))
    flag == 0
    if a + b > c and a + c > b and b + c > a:
        if (a ** 2 + b ** 2) - c ** 2 < 1e-5 or (b ** 2 + c ** 2) - a ** 2 < 1e-5 or (a ** 2 + b ** 2) - c ** 2 < 1e-5:
            flag = 1
            print("直角")
        if a == b or b == c or a == c:
            flag = 3
            print("等腰")

        print("三角形")
    else:
        print("不是三角形")


# test6()

def test7():
    sum1 = 0
    for i in range(101):
        if i % 7 == 0:
            sum1 += i

    print(sum1)


# test7()

sum1 = 0
for i in range(1001):
    if i % 7 == 0:
        sum1 += i
    elif "7" in str(i):
        sum1 += i
print(sum1)
