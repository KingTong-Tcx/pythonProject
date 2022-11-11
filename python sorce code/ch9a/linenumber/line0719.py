1   ﻿# program0719.py
2   filename=input("请输入要添加行号的文件名：")
3   filename2=input("请输入新生成的文件名：")
4   sourcefile=open(filename,'r',encoding="utf-8")
5   targetfile=open(filename2,'w',encoding="utf-8")
6   linenumber=""
7   for (num,value) in enumerate(sourcefile):
8       if num<9:
9           linenumber='0'+str(num+1)
10       else:
11           linenumber=str(num+1)
12       str1=linenumber+"   "+value
13       print(str1)
14       targetfile.write(str1)
15   sourcefile.close()
16   targetfile.close()
