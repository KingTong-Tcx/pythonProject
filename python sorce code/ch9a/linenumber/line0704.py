1  # program0704.py
2
f = open("test.txt", "r")
3
str1 = f.readline()
4
5
while str1 != "":  # �ж��ļ��Ƿ����
    6
print(str1)
7
str1 = f.readline()
8
f.close()
