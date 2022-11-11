import jieba

stopwords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()] 
combine_dict = {}

for line in open("tongyici.txt"):
    seperate_word = line.strip().split(",")
    num = len(seperate_word)
    for i in range(1, num):
        combine_dict[seperate_word[i]] = seperate_word[0]
print(combine_dict)

##article = open("sanguo20.txt", encoding='utf-8').read()
##words = jieba.lcut(article)
##f = ",".join(words)
##result = open("output.txt", "w",encoding='utf-8')
###result.write(f.encode("utf-8"))
##result.write(f)
##result.close()

result = open("output2.txt", "w",encoding='utf-8')
for line in open("sanguo20.txt", "r",encoding='utf-8'):
    line_1 = line.split(",")
    #print(line_1)

    final_sentence = ""

    for word in line_1:
        if word in combine_dict:
            word = combine_dict[word]
            final_sentence += word
        else:
            final_sentence += word
    result.write(final_sentence)

result.close()
   # print('111',final_sentence)
'''
##################
    words = jieba.lcut(final_sentence)
#print(words[:200])
    word_freq = {}
    for word in words:
        if (word in stopwords) or len(word)==1:
            continue
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

   # print(word_freq)
#  sorted    
freq_word = []
for word, freq in word_freq.items():
    freq_word.append((word, freq))
#print(freq_word[0])

freq_word.sort(key = lambda x:x[1], reverse=True)
max_number = eval(input("需要前多少位高频词？ "))
# display
for word, freq in freq_word[:max_number]:
    print(word, freq)
'''
