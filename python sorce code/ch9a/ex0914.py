# program0714.py
import os, os.path, sys

fname = input("请输入需要更名的文件:")
gname = input("请输入更名后的文件名:")
if not os.path.exists(fname):
    print("{}文件不存在".format(fname))
    sys.exit(0)
elif os.path.exists(gname):
    print("{}文件已存在".format(gname))
    sys.exit(0)
else:
    os.rename(fname, gname)
print("rename success")
