
 1   #program0304.py
 2   month=eval(input("请输入您选择的月份： "))
 3   days = 0;
 4   
 5   if (month ==1 or month == 3 or month == 5 or month == 7 or month == 8\
 6       or month == 10 or month == 12):
 7       days = 31
 8   elif(month == 4 or month == 6 or month == 9 or month == 11):
 9       days = 30
10   else:
11       days=28
12   print("{}月份的天数为{}".format(month,days))
