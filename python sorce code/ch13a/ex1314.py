#ex1314.py
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(6,4))      #创建绘图对象
x=np.arange(0,np.pi*4,0.01)
y=np.cos(x)
#plt.plot(x,y,"g-",linewidth=2.0)
plt.plot(x,y,color="g",ls='-.',linewidth=2.0)
plt.xlabel("x")               #x轴文字
plt.ylabel("cos(x)")          #y轴文字
plt.ylim(-1,1)                #y轴范围
plt.title("y=cos(x)")         #图表标题
plt.grid(True)
plt.show()

#plt.savefig("test.png", dpi=120)
