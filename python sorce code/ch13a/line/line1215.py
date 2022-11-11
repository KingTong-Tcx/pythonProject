1  # program1215.py
2
import numpy as np

3
import matplotlib.pyplot as plt

4
plt.figure(1)  # 创建图表1
5
ax1 = plt.subplot(211)  # 图表1中的子图1
6
ax2 = plt.subplot(212)  # 图表1中的子图2
7
plt.figure(2)  # 创建图表2
8
x = np.linspace(0, 3, 50)
9
for i in x:
10
plt.figure(2)  # 选择图表2
11
plt.plot(x, np.exp(i * x / 3))
12
plt.sca(ax1)  # 选择图表1的子图1
13
plt.plot(x, np.sin(i * x))
14
plt.sca(ax2)
15
plt.plot(x, np.cos(i * x))
16
plt.show()
17
18
