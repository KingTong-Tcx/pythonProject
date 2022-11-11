1  # program0714.py
2
import os, os.path, sys

3
fname = input("��������Ҫ�������ļ�:")
4
gname = input("�������������ļ���:")
5
if not os.path.exists(fname):
    6
print("{}�ļ�������".format(fname))
7
sys.exit(0)
8 elif os.path.exists(gname):
9
print("{}�ļ��Ѵ���".format(gname))
10
sys.exit(0)
11 else:
12
os.rename(fname, gname)
13
print("rename success")
