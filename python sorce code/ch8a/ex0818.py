# program0618.py
'''
使用jieba库分解中文文本，并使用字典实现词频统计,统计结果中排除
部分单词，被排除单词保存在文件stopwords.txt中
'''
import jieba
stopwords = [line.strip() for line in open('stopwords.txt', 'r', \
                                           encoding='utf-8').readlines()] 
#  add extra stopword
stopwords.append('')
# read need analyse file
article = open("sanguo60.txt", encoding='utf-8').read()
words = jieba.cut(article, cut_all = False)
#  count word freq
word_freq = {}
for word in words:
    if (word in stopwords) or len(word)==1:
        continue
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
#  sorted    
freq_word = []
for word, freq in word_freq.items():
    freq_word.append((word, freq))
freq_word.sort(key = lambda x:x[1], reverse=True)
max_number = eval(input("需要前多少位高频词？ "))
# display
for word, freq in freq_word[:max_number]:
    print(word, freq)
