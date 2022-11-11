1   # program0717.py
2   # 使用内置csv模块写入和读取二维数据
3   
4   datas = [['Name', 'DEP', 'Eng','Math', 'Chinese'],
5   ['Rose', '法学', 89, 78, 65],
6   ['Mike', '历史', 56,'', 44],
7   ['John', '数学', 45, 65, 67]
8   ]
9   
10   import csv
11   filename = 'bsheet.csv'
12   with open(filename, 'w',newline="") as f:
13       writer = csv.writer(f)
14       for row in datas:
15           writer.writerow(row)   
16   
17   ls=[]
18   with open(filename,'r') as f:
19       reader = csv.reader(f)
20       #print(reader)
21       for row in reader:
22           print(reader.line_num, row)    # 行号从1开始
23           ls.append(row)
24       print(ls)
25           
26   
27   
28   
