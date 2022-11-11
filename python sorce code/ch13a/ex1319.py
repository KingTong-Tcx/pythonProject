#program1219.py
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']='SimHei'
labels=["一季度","二季度","三季度","四季度"]
data=(16,27,25,29)
explodes=[0,0.1,0.1,0]
plt.axes(aspect=1)
plt.pie(x=data,labels=labels,explode=explodes,autopct="%.1f%%",shadow=True)
plt.show()

