1  # program0617.py
2
'''
3   使用jieba库分解中文文本，并使用字典实现词频统计
4   '''
5  # encoding=utf-8
6
import jieba

7  # read need analyse file
8
article = open("sanguo60.txt", encoding='utf-8').read()
9
words = jieba.lcut(article)
10  # count word freq
11
word_freq = {}
12
for word in words:
    13
if len(word) == 1:
    14
continue
15 else:
16
word_freq[word] = word_freq.get(word, 0) + 1
17  # sorted
18
freq_word = []
19
for word, freq in word_freq.items():
    20
freq_word.append((word, freq))
21
freq_word.sort(key=lambda x: x[1], reverse=True)
22
max_number = eval(input("显示前多少位高频词？ "))
23  # display
24
for word, freq in freq_word[:max_number]:
    25
print(word, freq)
