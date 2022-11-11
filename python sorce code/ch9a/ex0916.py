# program0716.py
# 向CSV文件中写入一维数据并读取
lst1 = ["name","age","school","address"]
filew= open('asheet.csv', 'w')
filew.write(",".join(lst1))
filew.close()

filer= open('asheet.csv', 'r')
line=filer.read()
print(line)
filer.close()

