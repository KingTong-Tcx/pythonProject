# program1215.py
import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)  # 创建图表1
ax1 = plt.subplot(211)  # 图表1中的子图1
ax2 = plt.subplot(212)  # 图表1中的子图2
plt.figure(2)  # 创建图表2
x = np.linspace(0, 3, 50)
for i in x:
    plt.figure(2)  # 选择图表2
    plt.plot(x, np.exp(i * x / 3))
    plt.sca(ax1)  # 选择图表1的子图1
    plt.plot(x, np.sin(i * x))
    plt.sca(ax2)
    plt.plot(x, np.cos(i * x))
plt.show()
