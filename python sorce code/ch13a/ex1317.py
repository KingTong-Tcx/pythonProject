# program1217.py
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6, 4))
y = [10, 20, 8.45, 22, 3, 2, 12]
x = np.arange(7)
plt.bar(x, y, color="blue", width=0.5)
plt.show()
