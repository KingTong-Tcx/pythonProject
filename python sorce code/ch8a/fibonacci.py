#fibonacci.py
def fibo1(x):   #返回小于x的契波那契数列的所有项
    a,b=0,1
    while b<=x:
        print(b,end=" ")
        a,b=b,a+b
def fibo2(x):  #返回小于x的契波那契数列的最大项
    a,b=0,1
    while b<x:
        a,b=b,a+b
    print(a)
if __name__=="__main__":
    print("please me as a module.")
