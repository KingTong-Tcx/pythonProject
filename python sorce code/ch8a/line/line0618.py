1  # program0618.py
2
'''
3   使用jieba库分解中文文本，并使用字典实现词频统计,统计结果中排除
4   部分单词，被排除单词保存在文件stopwords.txt中
5   '''
6
import jieba

7
stopwords = [line.strip() for line in open('stopwords.txt', 'r', \
                                           8
encoding = 'utf-8').readlines()]
9  # add extra stopword
10
stopwords.append('')
11  # read need analyse file
12
article = open("sanguo60.txt", encoding='utf-8').read()
13
words = jieba.cut(article, cut_all=False)
14  # count word freq
15
word_freq = {}
16
for word in words:
    17
if (word in stopwords) or len(word) == 1:
    18
continue
19
if word in word_freq:
    20
word_freq[word] += 1
21 else:
22
word_freq[word] = 1
23  # sorted
24
freq_word = []
25
for word, freq in word_freq.items():
    26
freq_word.append((word, freq))
27
freq_word.sort(key=lambda x: x[1], reverse=True)
28
max_number = eval(input("需要前多少位高频词？ "))
29  # display
30
for word, freq in freq_word[:max_number]:
    31
print(word, freq)
