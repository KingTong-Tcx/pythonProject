1  # program0105.py
2
'''
3   ���������������ߣ��к��׹�ʽ�������������s��
4   �ڶ����߽������쳣��������ϣ��ж�3�߷���������������
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
11   except NameError:
12
print("������������ֵ")
13
if a < 0 or b < 0 or c < 0:
    14
print("�������ݲ�����Ϊ����")
15 elif a + b <= c or a + c <= b or b + c <= a:
16
print("����������֮�ʹ��ڵ�����ԭ��")
17 else:
18
p = (a + b + c) / 2
19
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
20
print("�����ε������{:.2f}".format(s))
