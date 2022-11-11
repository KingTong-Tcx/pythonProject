1  # program0707.py
2
f1 = open("d:\\pythonfile36\\data7.dat", "a")
3
lst = ["HTML5", "CSS3", "Javascript"]
4
tup1 = ('2012', '2010', '1990')
5
m1 = {"name": "John", "City": "SH"}
6
f1.writelines(lst)
7
f1.writelines('\n')
8
f1.writelines(tup1)
9
f1.writelines('\n')
10
f1.writelines(m1)
11
f1.close()
