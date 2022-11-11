1  # program1219.py
2
import matplotlib

3
import matplotlib.pyplot as plt

4
5
matplotlib.rcParams['font.family'] = 'SimHei'
6
matplotlib.rcParams['font.sans-serif'] = 'SimHei'
7
labels = ["一季度", "二季度", "三季度", "四季度"]
8
data = [16, 27, 25, 29]
9
explodes = [0, 0.1, 0.1, 0]
10
plt.axes(aspect=1)
11
plt.pie(x=data, labels=labels, explode=explodes, autopct="%.1f%%", shadow=True)
12
plt.show()
13
