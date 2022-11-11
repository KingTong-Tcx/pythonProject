# ex0907.py
f1 = open("d:\\python36\\data7.dat", "a")
lst = ["HTML5", "CSS3", "Javascript"]
tup1 = ('2012', '2010', '1990')
m1 = {"name": "John", "City": "SH"}
f1.writelines(lst)
f1.writelines('\n')
f1.writelines(tup1)
f1.writelines('\n')
f1.writelines(m1)
f1.close()
