 1   #program1218.py
 2   import matplotlib.pyplot as plt
 3   import numpy as np
 4   plt.figure(figsize=(8,6))
 5   x=np.random.randint(10,20,20)
 6   y1=np.random.randint(10,30,20)
 7   y2=np.random.randint(10,30,20)
 8   plt.ylim(0,70)   # 设置Y轴的显示范围
 9   #上部的条形图
10   plt.bar(x,y1,width=0.5,color="red",label="$y1$")  
11   #底部的条形图
12   plt.bar(x,y2,bottom=y1,width=0.5,color="blue",label="$y2$")
13   plt.legend()
14   plt.show()
15   
