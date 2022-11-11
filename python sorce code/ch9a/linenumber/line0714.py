1   #program0714.py 
2   import os,os.path,sys
3   fname=input("请输入需要更名的文件:")
4   gname=input("请输入更名后的文件名:")
5   if not os.path.exists(fname):
6       print("{}文件不存在".format(fname))
7       sys.exit(0)
8   elif os.path.exists(gname):
9       print("{}文件已存在".format(gname))
10       sys.exit(0)
11   else:
12       os.rename(fname,gname)
13   print("rename success")
