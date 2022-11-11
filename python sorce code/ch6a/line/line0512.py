
 1   #program0512.py
 2   def findwords(sentence):
 3       "统计参数中含有字符e的单词，保存到列表中，并返回"
 4       result=[]
 5       words=sentence.split()
 6       for word in words:
 7           if word.find("e")!=-1:
 8               result.append(word)
 9   
10       return result
11   
12   ss="Return the lowest index in S where substring sub is found,"
13   print(findwords(ss))
