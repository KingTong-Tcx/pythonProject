#program0311.py
k=eval(input("请输入计算阶乘的数值： "))
sum1 = 0
i=1
while i<=k:
    t=j=1
    while j<=i:
        t*=j
        j+=1
    
    sum1+=t
    i+=1

print(sum1)
