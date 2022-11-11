#progarm0903.py
from tkinter import *
win=Tk()
label = Label()
label.config(text="Hello Python")    #配置文本属性
label.config(fg="white",bg="blue")   #配置前景和背景属性
label.pack()
btn1= Button()
btn1['text']="click"                    #配置文本属性的另一种方法
btn1.pack()
win.title("配置组件属性")    #title()方法
win.geometry("300x200")    #geometry()方法
win.mainloop()
