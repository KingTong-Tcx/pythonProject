
 1   #program1216.py
 2   import matplotlib.pyplot as plt
 3   import numpy as np
 4   mu=100       #设置起始值
 5   sigma=20     #每个点的放大倍数
 6   x=mu+sigma*np.random.randn(20)   #为简单直观，样本量取20
 7   plt.hist(x,bins=10,color='green',density=False)
 8   print(x)
 9   plt.show()
10   #plt.hist(x,bins=30,color='green',density=True)
11   
