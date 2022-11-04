# 3.3
def factorial(n):
    return n * n


k = 100
sum1 = 0
for i in range(1, k):
    if i % 2 == 0:
        sum1 -= factorial(i)
    else:
        sum1 += factorial(i)
print(sum1)
