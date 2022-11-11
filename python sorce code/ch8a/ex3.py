import jieba

stopwords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()] 
combine_dict = {}

for line in open("tongyici.txt"):
    seperate_word = line.strip().split(",")
    num = len(seperate_word)
    for i in range(1, num):
        combine_dict[seperate_word[i]] = seperate_word[0]
print(combine_dict)

article = open("sanguo20.txt", encoding='utf-8').read()
words = jieba.lcut(article)
f = ",".join(words)
result = open("output.txt", "w",encoding='utf-8')
#result.write(f.encode("utf-8"))
result.write(f)
result.close()

result = open("exex2.txt", "w", encoding='utf-8')
for line in open("ex.txt", "r", encoding='utf-8'):
    line_1 = line.split(",")
    #print(line_1)

    final_sentence = ""

    for word in line_1:
        if word in combine_dict:
            word = combine_dict[word]
            final_sentence += word
        else:
            final_sentence += word
    print( final_sentence)
    #result.write(final_sentence)

result.close()
