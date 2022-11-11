#program0319.py
n=eval(input("请输入打印的行数： "))
for x in range(1,n+1):
    print(' '*(10-x),end="")
    n=x
    while n>=1:
        print(n,sep="",end="")
        n-=1
   
    n=2
    while n<=x:
        print(n,sep="",end="")
        n+=1
    print()
