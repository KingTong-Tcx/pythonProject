# 30个阶梯，你一次可以上一阶或两阶，走上去，共有多少种走法？
# 题目分析
# 由题意可知，一次可以上一阶或两阶阶梯，由此可以列出当有一阶，两阶，三阶，四阶，五阶…它们的走法，可以推导出递推公式。
# 因为只能是一阶一阶上或者两阶两阶上，所以到达顶点的最后一步不是一阶就是两阶,倒数第二步也是这样
#  边界条件：当阶梯数为1和0时，都只有一种走法
# 递推公式：step(n)=step(n-1)+step(n-2)
def step(n):
    if n <= 1:
        return 1
    else:
        return step(n - 1) + step(n - 2)


n = eval(input())
print(step(n))

print("------------------------------------------------------")


def step1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return step(n - 1) + step(n - 2)


a = 30
print(step1(a))
