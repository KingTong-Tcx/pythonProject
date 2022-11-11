#program0521.py
basis=100            #全局变量
def func3(x,y):
    basis=90         #与全局变量同名，但是局部变量，与全局变量无关
    sum=basis+x+y
    return sum

print("{:6.2f}".format(func3(75,62)))
print(basis)         #全局变量值仍为100
print("------------------------")
