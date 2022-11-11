#program0720.py
from datetime import datetime
filename=input("请输入日志文件名：")
file=open(filename,'a')
print("请输入日志，exit结束")
s=input("log:")
while s.lower()!="exit":
    file.write("\n"+s)
    file.write("\n----------------------\n")
    file.flush()
    s=input("log:")
file.write("\n====="+str(datetime.now())+"=====\n")
file.close()
