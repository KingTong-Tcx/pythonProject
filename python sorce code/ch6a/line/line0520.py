
 1   #program0520.py
 2   basis=100            #全局变量
 3   def func1(x,y):     #计算总分
 4       sum=basis+x+y
 5       return sum
 6   
 7   def func2(x,y):      #按某规则计算平均分
 8       avg=(basis+x*0.9+y*0.8)/3
 9       return avg
10   
11   score1=func1(75,62)
12   score2=func2(75,62)
13   print("{:6.2f},{:6.2f}".format(score1,score2))
14   print(basis)
15   print("------------------------")
