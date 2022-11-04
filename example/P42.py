# 2编写程序，给出一个字符串，将其中的字符"E"用空格替换后输出
str1 = "abcdeABCDE"
print(str1.replace("E", " "))

# 3从键盘交互式输入一个人的18未生份证号，类似于"2001年9月12日"的形式输出该人的出生日期
idcard = input("请输入你的身份证号码:")
year = idcard[6:10]
month = idcard[10:12]
day = idcard[12:14]
sex = idcard[16:17]
print("你的生日：%s年是%s月%s日." % (year, month, day))
