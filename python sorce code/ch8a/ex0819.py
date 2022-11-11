# program0619.py
'''
使用jieba库分解中文文本，并使用字典实现词频统计,统计结果中排除
部分单词，被排除单词保存在文件stopwords.txt中，合并了部分同义词
'''
import jieba
stopwords=[line.strip() for line in open('stopwords.txt', \
                                         encoding='utf-8').readlines()] 
#  add extra stopword
stopwords.append('')
# read need analyse file
article = open("sanguo60.txt", encoding='utf-8').read()
words = jieba.lcut(article)
#  count word freq
word_freq = {}
for word in words:
    if (word in stopwords) or len(word)==1:
        continue
    elif word=='玄德' or word=='玄德曰':
        newword='刘备'
    elif word=='关公' or word=='云长':
        newword='关羽'
    elif word=='丞相':
        newword='曹操'
    elif word=='孔明' or word=='孔明曰':
        newword='诸葛亮'
    else:
         newword=word
         
    if newword in word_freq:
        word_freq[newword] += 1
    else:
        word_freq[newword] = 1
#  sorted    
freq_word = []
for word, freq in word_freq.items():
    freq_word.append((word, freq))
freq_word.sort(key = lambda x:x[1], reverse=True)
max_number = eval(input("需要前多少位高频词？ "))
# display
for word, freq in freq_word[:max_number]:
    print(word, freq)
