# program0809.py
def payOut(quota):
    if (quota > 5000):
        raise ValueError("The quota out of bounds!")
    else:
        return quota - quota * 0.1


pay = payOut(4000)
print("实际支出金额是：", pay)
pay = payOut(5200)
print("实际支出金额是：", pay)
