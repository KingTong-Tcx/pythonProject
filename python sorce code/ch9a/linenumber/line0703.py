1   #program0703.py
2   f=open("test.txt","r")
3   flist=f.readlines()       # flist是包含文件内容的列表
4   print(flist)
5   for line in flist:
6       print(line)           #使用print(line,end="")将不显示文件中的空行。
7   f.close()
