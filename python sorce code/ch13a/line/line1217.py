
 1   #program1217.py
 2   import matplotlib.pyplot as plt
 3   import numpy as np
 4   plt.figure(figsize=(6,4))
 5   y=[10,20,8.45,22,3,2,12]
 6   x=np.arange(7)
 7   plt.bar(x,y,color="blue",width=0.5)
 8   plt.show()
