
 1   #program0310.py
 2   k=eval(input("请输入计算阶乘的数值:"))
 3   sum1=0
 4   for i in range(1,k):
 5       t = 1
 6       for j in range(1,i+1):
 7           t *= j
 8       sum1 += t
 9   print(sum1)
