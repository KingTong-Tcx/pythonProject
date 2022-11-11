1  # program0417.py
2
sentence = 'Beautiful is better than ugly.Explicit is better than implicit.\
 3   Simple is better than complex.Complex is better than complicated.'
4  # 将文本中涉及标点用空格替换
5
for ch in ",.?!":
    6
sentence = sentence.replace(ch, " ")
7  # 利用字典统计词频
8
words = sentence.split()
9
map1 = {}
10
for word in words:
    11
if word in map1:
    12
map1[word] += 1
13 else:
14
map1[word] = 1
15  # 对统计结果排序
16
items = list(map1.items())
17
items.sort(key=lambda x: x[1], reverse=True)
18  # 打印控制
19
for item in items:
    20
word, count = item
21
print("{:<12}{:>5}".format(word, count))
