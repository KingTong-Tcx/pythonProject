# program0717.py
# 使用内置csv模块写入和读取二维数据

datas = [['Name', 'DEP', 'Eng','Math', 'Chinese'],
['Rose', '法学', 89, 78, 65],
['Mike', '历史', 56,'', 44],
['John', '数学', 45, 65, 67]
]

import csv
filename = 'bsheet.csv'
with open(filename, 'w',newline="") as f:
    writer = csv.writer(f)
    for row in datas:
        writer.writerow(row)   

ls=[]
with open(filename,'r') as f:
    reader = csv.reader(f)
    #print(reader)
    for row in reader:
        print(reader.line_num, row)    # 行号从1开始
        ls.append(row)
    print(ls)
        



