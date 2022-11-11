1  # program0703.py
2
f = open("test.txt", "r")
3
flist = f.readlines()  # flist�ǰ����ļ����ݵ��б�
4
print(flist)
5
for line in flist:
    6
print(line)  # ʹ��print(line,end="")������ʾ�ļ��еĿ��С�
7
f.close()
