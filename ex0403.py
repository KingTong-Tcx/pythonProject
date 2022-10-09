# ex0403.py
flag = 1        # flag=1 表示有会员卡
books = 8       # 购书数量
price = 234     # 单价
actualPay = 0

if flag == 1:
    if books >= 5:
        actualPay = price * 0.75 * books
    else:
        actualPay = price * 0.85 * books
else:
    if books >= 5:
        actualPay = price * 0.85 * books
    else:
        actualPay = price * 0.95 * books

print("您的实际付款金额是： ", actualPay)
