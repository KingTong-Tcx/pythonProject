
 1   #program0305.py
 2   flag=1            # flag=1表示有会员卡
 3   books=8           # 购书数量
 4   payaccount=234   # 应付金额
 5   actualpay=0
 6   
 7   if flag==1:
 8       if books>=5:
 9           actualpay=payaccount*0.75
10       else:
11           actualpay=payaccount*0.85
12   else:
13       if books>=5:
14           actualpay=payaccount*0.85
15       else:
16           actualpay=payaccount*0.95
17              
18   print("您的实际付款金额是： ",actualpay)
