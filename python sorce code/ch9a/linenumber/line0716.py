1   # program0716.py
2   # 向CSV文件中写入一维数据并读取
3   lst1 = ["name","age","school","address"]
4   filew= open('asheet.csv','w')
5   filew.write(",".join(lst1))
6   filew.close()
7   
8   filer= open('asheet.csv','r')
9   line=filer.read()
10   print(line)
11   filer.close()
12   
