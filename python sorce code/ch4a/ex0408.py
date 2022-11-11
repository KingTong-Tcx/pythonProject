#program0310.py
k=eval(input("请输入计算阶乘的数值:"))
sum1=0
for i in range(1,k):
    t = 1
    for j in range(1,i+1):
        t *= j
    sum1 += t
print(sum1)
