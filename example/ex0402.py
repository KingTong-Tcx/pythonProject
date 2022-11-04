# ex0402.py
# 判断闰年：四年一闰，百年不闰；四百年再闰
year = eval(input("请输入您选择的年份： "))
month = eval(input("请输入您选择的月份： "))
days = 0;
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    if month == 2:
        days = 29
else:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    else:
        days = 28

print("{}月份的天数为{}".format(month, days))
