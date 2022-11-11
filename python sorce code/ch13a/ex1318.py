#program1218.py
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(8,6))
x=np.random.randint(10,20,20)
y1=np.random.randint(10,30,20)
y2=np.random.randint(10,30,20)
plt.ylim(0,70)   # 设置Y轴的显示范围
#上部的条形图
plt.bar(x,y1,width=0.5,color="red",label="$y1$")  
#底部的条形图
plt.bar(x,y2,bottom=y1,width=0.5,color="blue",label="$y2$")
plt.legend()
plt.show()

