# program0417.py
sentence = 'Beautiful is better than ugly.Explicit is better than implicit.\
Simple is better than complex.Complex is better than complicated.'
# 将文本中涉及标点用空格替换
for ch in ",.?!":
    sentence = sentence.replace(ch, " ")
# 利用字典统计词频
words = sentence.split()
map1 = {}
for word in words:
    if word in map1:
        map1[word] += 1
    else:
        map1[word] = 1
# 对统计结果排序
items = list(map1.items())
items.sort(key=lambda x: x[1], reverse=True)
# 打印控制
for item in items:
    word, count = item
    print("{:<12}{:>5}".format(word, count))
