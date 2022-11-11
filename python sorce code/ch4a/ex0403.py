#program0305.py
flag=1            # flag=1表示有会员卡
books=8           # 购书数量
payaccount=234   # 应付金额
actualpay=0

if flag==1:
    if books>=5:
        actualpay=payaccount*0.75
    else:
        actualpay=payaccount*0.85
else:
    if books>=5:
        actualpay=payaccount*0.85
    else:
        actualpay=payaccount*0.95
           
print("您的实际付款金额是： ",actualpay)
