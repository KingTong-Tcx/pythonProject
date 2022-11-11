1  # program0718.py
2  # ʹ������csvģ��д��Ͷ�ȡ��ά����
3
datas = [['Name', 'DEP', 'Eng', 'Math', 'Chinese'],
         4['Rose', '��ѧ', 89, 78, 65],
         5['Mike', '��ʷ', 56, '', 44],
         6['John', '��ѧ', 45, 65, 67]
         7]
8
import csv

9
filename = 'bsheet.csv'
10
str1 = ''
11
with open(filename, 'r') as f:
    12
reader = csv.reader(f)
13  # print(reader)
14
for row in reader:
    15
for item in row:
    16
str1 += item + '\t'
17
str1 += '\n'
18
print(reader.line_num, row)  # �кŴ�1��ʼ
19
print(str1)
20
21
22
