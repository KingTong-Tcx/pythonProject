# ex0406.py
def factorial(n):
    t = 1
    for i in range(1, n + 1):
        t = t * i
    return t


k = 6
sum1 = 0
for i in range(1, k):
    sum1 += factorial(i)
print("1!+2!+...+5!=", sum1)
