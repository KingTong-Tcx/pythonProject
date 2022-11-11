import csv

filename = 'sheet.csv'
ls = []
with open(filename, 'r') as f:
    reader = csv.reader(f)
    # print(reader)
    for row in reader:
        # 行号从1开始
        print(reader.line_num, row)
        # ls.append(row)
    print(ls)

########################################
##import csv
##
### 使用数字和字符串的数字都可以
##datas = [['name', 'age'],
##         ['Bob', 14],
##         ['Tom', 23],
##        ['Jerry', '18']]
##
##with open('example.csv', 'w') as f:
##    writer = csv.writer(f)
##    for row in datas:
##        writer.writerow(row)
##        
##    # 还可以写入多行
##    #writer.writerows(datas)
