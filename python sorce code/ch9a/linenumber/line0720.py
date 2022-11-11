1   #program0720.py
2   from datetime import datetime
3   filename=input("请输入日志文件名：")
4   file=open(filename,'a')
5   print("请输入日志，exit结束")
6   s=input("log:")
7   while s.lower()!="exit":
8       file.write("\n"+s)
9       file.write("\n----------------------\n")
10       file.flush()
11       s=input("log:")
12   file.write("\n====="+str(datetime.now())+"=====\n")
13   file.close()
