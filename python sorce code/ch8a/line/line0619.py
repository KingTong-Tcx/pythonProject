
 1   # program0619.py
 2   '''
 3   使用jieba库分解中文文本，并使用字典实现词频统计,统计结果中排除
 4   部分单词，被排除单词保存在文件stopwords.txt中，合并了部分同义词
 5   '''
 6   import jieba
 7   stopwords=[line.strip() for line in open('stopwords.txt',\
 8                                            encoding='utf-8').readlines()] 
 9   #  add extra stopword
10   stopwords.append('')
11   # read need analyse file
12   article = open("sanguo60.txt",encoding='utf-8').read()
13   words = jieba.lcut(article)
14   #  count word freq
15   word_freq = {}
16   for word in words:
17       if (word in stopwords) or len(word)==1:
18           continue
19       elif word=='玄德' or word=='玄德曰':
20           newword='刘备'
21       elif word=='关公' or word=='云长':
22           newword='关羽'
23       elif word=='丞相':
24           newword='曹操'
25       elif word=='孔明' or word=='孔明曰':
26           newword='诸葛亮'
27       else:
28            newword=word
29            
30       if newword in word_freq:
31           word_freq[newword] += 1
32       else:
33           word_freq[newword] = 1
34   #  sorted    
35   freq_word = []
36   for word, freq in word_freq.items():
37       freq_word.append((word, freq))
38   freq_word.sort(key = lambda x:x[1], reverse=True)
39   max_number = eval(input("需要前多少位高频词？ "))
40   # display
41   for word, freq in freq_word[:max_number]:
42       print(word, freq)
