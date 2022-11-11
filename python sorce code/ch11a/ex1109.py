#progarm0909.py
from tkinter import *
str='标签基本属性测试'
mylabel=Label(text=str)
mylabel.config(justify=CENTER)		#设置文本居中对齐
mylabel.config(width=20,height=4)	#设置标签的宽和高，单位为字符个数
mylabel.config(bd=2,relief=SOLID)       #设置边框宽度
mylabel.config(wraplength=140)		#设置文字回卷宽度为160像素
mylabel.config(anchor=W)		#设置内容在标签内部的左侧
mylabel.config(font=('宋体',18))	       #设置字体
mylabel.pack(side=TOP) 			#设置标签在窗口的左侧
mainloop()
