1   # program0101.py
2   # ���������������ߣ��к��׹�ʽ�������������s��
3   import math
4   a=eval(input("������a�߳���"))
5   b=eval(input("������b�߳���"))
6   c=eval(input("������c�߳���"))
7   p = (a + b + c) / 2
8   s = math.sqrt(p * (p - a) * (p - b) * (p - c))
9   print("�����ε������{:.2f}".format(s))
