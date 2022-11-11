# program0704.py
f = open("test.txt", "r")
str1 = f.readline()

while str1 != "":  # 判断文件是否结束
    print(str1)
    str1 = f.readline()
f.close()
