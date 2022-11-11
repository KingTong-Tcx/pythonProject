#program0517.py
def factorial(i):
    "求指定参数的阶乘"
    t=1
    for i in range(1,i+1):
        t*=i
    return t

print(factorial(6))      #720
