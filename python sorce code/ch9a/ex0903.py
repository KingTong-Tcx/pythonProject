# program0703.py
f = open("test.txt", "r")
flist = f.readlines()  # flist是包含文件内容的列表
print(flist)
for line in flist:
    print(line)  # 使用print(line,end="")将不显示文件中的空行。
f.close()
