import jieba
combine_dict = {}

for line in open("tyc.txt", "r"):
    seperate_word = line.strip().split(",")
    num = len(seperate_word)
    for i in range(1, num):
        combine_dict[seperate_word[i]] = seperate_word[0]
print(combine_dict)

jieba.suggest_freq("北平城", tune = True)
seg_list = jieba.lcut("北京是中国的首都，京城的景色非常优美，就像当年的北平城，我爱这故都的一草一木。\n察运行结运行结运行结运行结运行结果，可以看出，")
f = ",".join(seg_list)
result = open("output.txt", "w")
#result.write(f.encode("utf-8"))
result.write(f)

result.close()

for line in open("output.txt", "r"):
    line_1 = line.split(",")

final_sentence = ""
for word in line_1:
    if word in combine_dict:
        word = combine_dict[word]
        final_sentence += word
    else:
        final_sentence += word
print(final_sentence)

'''
stopwords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()] 
##################
words = jieba.lcut(final_sentence)
word_freq = {}
for word in words:
    if word in stopwords or len(word)==1:
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
max_number = int(input("需要前多少位高频词？ "))
# display
for word, freq in freq_word[:max_number]:
    
    print(word, freq)
    '''
