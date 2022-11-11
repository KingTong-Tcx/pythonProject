
 1   #program1214.py
 2   import matplotlib.pyplot as plt
 3   import numpy as np
 4   plt.figure(figsize=(6,4))      #创建绘图对象
 5   x=np.arange(0,np.pi*4,0.01)
 6   y=np.cos(x)
 7   plt.plot(x,y,"g-",linewidth=2.0)
 8   plt.xlabel("x")               #x轴文字
 9   plt.ylabel("cos(x)")          #y轴文字
10   plt.ylim(-1,1)                #y轴范围
11   plt.title("y=cos(x)")         #图表标题
12   plt.grid(True)
13   plt.show()
14   
15   #plt.savefig("test.png", dpi=120)
