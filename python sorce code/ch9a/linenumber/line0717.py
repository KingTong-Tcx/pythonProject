1  # program0717.py
2  # ʹ������csvģ��д��Ͷ�ȡ��ά����
3
4
datas = [['Name', 'DEP', 'Eng', 'Math', 'Chinese'],
         5['Rose', '��ѧ', 89, 78, 65],
         6['Mike', '��ʷ', 56, '', 44],
         7['John', '��ѧ', 45, 65, 67]
         8]
9
10
import csv

11
filename = 'bsheet.csv'
12
with open(filename, 'w', newline="") as f:
    13
writer = csv.writer(f)
14
for row in datas:
    15
writer.writerow(row)
16
17
ls = []
18
with open(filename, 'r') as f:
    19
reader = csv.reader(f)
20  # print(reader)
21
for row in reader:
    22
print(reader.line_num, row)  # �кŴ�1��ʼ
23
ls.append(row)
24
print(ls)
25
26
27
28
