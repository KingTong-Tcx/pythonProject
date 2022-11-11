1  # program0104.py
2
'''
3    ���������������ߣ��к��׹�ʽ�������������s��
4     �����߽������쳣����
5   '''
6
import math

7
try:
    8
a = eval(input("������a�߳���"))
9
b = eval(input("������b�߳���"))
10
c = eval(input("������c�߳���"))
11
p = (a + b + c) / 2
12
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
13
print("�����ε������{:.2f}".format(s))
14   except NameError:
15
print("������������ֵ")
