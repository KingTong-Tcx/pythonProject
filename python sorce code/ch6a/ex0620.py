#program0520.py
basis=100            #全局变量
def func1(x,y):     #计算总分
    sum=basis+x+y
    return sum

def func2(x,y):      #按某规则计算平均分
    avg=(basis+x*0.9+y*0.8)/3
    return avg

score1=func1(75,62)
score2=func2(75,62)
print("{:6.2f},{:6.2f}".format(score1,score2))
print(basis)
print("------------------------")
