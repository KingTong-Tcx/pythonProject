1   # program0108.py
2   file=open("file.txt",'r')
3   s1=file.read()
4   file.close()
5   lst=s1.split(',')
6   lst2=[]
7   for item in lst:
8       lst2.append(eval(item))
9   #print(lst2)
10   #notpass为不及格人数，maxscore为最高分
11   notpass =maxscore= 0 
12   for item in lst2:   
13       if maxscore<item:
14           maxscore=item
15       if item<60:
16           notpass+=1
17   print("最高分是{}，不及数人数是{}".format(maxscore,notpass))
18   
