import random


def test1():
    # 字符串s1 = 'ABC',字符串s2=‘123', 要求：生成序列A1A2A3B1B2B3C1C2C3
    s1 = "ABC"
    s2 = "123"
    list1 = []
    for i in range(len(s1)):
        for j in range(len(s2)):
            list1.append(s1[i] + s2[j])
    print(list1)


# test1()

def test2():
    # 有1、2、3、4个数字，能组成多少个三位数？都是多少？
    lst1 = []
    sum1 = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in "1234":
                lst1.append(i * 100 + j * 10 + int(k))
                sum1 += 1
    print(lst1)
    print(sum1)


# test2()

def test3():
    # 有1、2、3、4个数字，能组成多少个互不相同目无重复数字的三位数？都是多少
    lst1 = []
    sum1 = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in "1234":
                if i != j and j != int(k) and i != int(k):
                    lst1.append(i * 100 + j * 10 + int(k))
                    sum1 += 1
    print(lst1)
    print(sum1)


# test3()
def book_p69_1():
    # p69-1
    # lst1 = []
    # sum1 = 0
    # str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    a = ""
    yzm = ""
    for i in range(0, 26):
        a = a + chr(65 + i)
    for i in range(0, 26):
        a = a + chr(97 + i)
    for i in range(0, 10):
        a = a + chr(48 + i)
    for i in range(4):
        yzm = yzm + a[random.randint(0, 63)]
    print(yzm)


# book_p69_1()
def test4():
    # 将一个正整数分解质因数。例如：输入90，打印出90=2*3*3*5。
    n = num = int(input("请输入一个数："))
    zys = []
    for i in range(2, int(num // 2 + 1)):
        flag = True
        while flag:
            if n % i == 0:
                n = n // i
                zys.append(i)
            else:
                flag = False
        if n == 1:
            break
    if len(zys) == 0:
        print("这没有质因数")
    else:
        print("%d=%d" % (num, zys[0]), end="")
        for i in range(1, len(zys)):
            print("*%d" % zys[i], end="")


test4()


def test5():
    # 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
    tmpStr = input('请输入字符串：')
    alphaNum = 0
    numbers = 0
    spaceNum = 0
    otherNum = 0
    for i in tmpStr:
        if i.isalpha():
            alphaNum += 1
        elif i.isnumeric():
            numbers += 1
        elif i.isspace():
            spaceNum += 1
        else:
            otherNum += 1
    print('字母=%d' % alphaNum)
    print('数字=%d' % numbers)
    print('空格=%d' % spaceNum)
    print('其他=%d' % otherNum)


# test5()
def test6():
    # 如果两个素数之差为2，这样的两个素数就叫作"李生数"，找出100以内的所有"孪生数.
    print('0到100以内的孪生数对有：')
    m = 2
    for num in range(3, 100, 2):
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                break
        else:
            if num - m == 2:
                print(f'({m},{num})')
            m = num


# test6()


def test7():
    # 输入一组数到列表nums,,请找到列表中任意两个元素相加能够等于9的元素，形成二个元组，使其小数在前，大数在后，如：（2,7),(1,8),重复的元组只保留一个，结果按元组第一个元素从小到大排序输出
    nums = [1, 2, 5, 6, 7, 8, 9, 0, -1, 1, -3, 10, 13, 4, 5, 3, 3, 4]
    lst = []
    for i in range(len(nums)):
        if 9 - nums[i] in nums:
            if 9 - nums[i] > nums[i]:
                b = (nums[i], 9 - nums[i])
            else:
                b = (9 - nums[i], nums[i])
            if b not in lst:
                lst.append(b)
    lst.sort(key=lambda x: x[0])
    print(lst)


# test7()
def test8():
    # 2【问题描述】
    # 定义一个电话簿，里头设置以下联系人：
    # 'mayun':13309283335',
    # 'zhaolong':'18989227822',
    # 'zhangmin':13382398921',
    # Gorge:'19833824743,
    # 'Jordan':'18807317878,
    # Curry':'15093488129',
    # Wade':'19282937665
    # 现在输入人名，查询他的号码。
    dic = {'mayun': '13309283335', 'zhaolong': '18989227822', 'zhangmin': '13382398921', 'Gorge': '19833824743',
           'Jordan': '18807317878', 'Curry': '15093488129', 'Wade': '19282937665'}
    a = input("请输入一个人名：")
    if a in dic.keys():
        print("%s的电话号码为：%s" % (a, dic[a]))
    else:
        print("没有这个人的电话号码")


# test8()
def test9():
    # 给定个整数，请统计出每个整数出现的次数，按出现次数从多到少的顺序输出。
    # 【输入形式】
    # 第一行包含一个整数n,表示给定数字的个数；第二行包含个整数，相邻的整数之间用一个空格分
    # 隔，表示所给定的整数。
    # 【输出形式】
    # 输出有多行，每行包含两个整数，分别表示一个给定的整数和它出现的次数。按出现次数递减的顺序
    # 输出。如果两个整数出现的次数一样多，则先输出值较小的，然后输出值较大的。
    st = [1, 2, 5, 6, 7, 8, 9, 0, -1, 1, -3, 10, 13, 4, 5, 3, 3, 4]
    dic = {}
    for i in range(len(st)):
        if st[i] in dic.keys():
            dic[st[i]] += 1
        else:
            dic[st[i]] = 1
    lst = []
    for item in dic.items():
        lst.append(item)
    lst.sort(key=lambda x: (x[1], x[0]), reverse=True)
    print(lst)
    for i in lst:
        print("%d 数出现的次数为： %d" % (i[0], i[1]))

# test9()
