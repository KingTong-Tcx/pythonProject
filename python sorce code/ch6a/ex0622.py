#program0522.py
basis=100            #全局变量
def func4(x,y):
    print(basis)
    basis=90
    sum=basis+x+y
    return sum

print(func4(78,62))
print(basis)
