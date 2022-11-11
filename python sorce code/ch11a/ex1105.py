#progarm0905.py
from tkinter import *
win=Tk()
label1 = Label(win,text="标签标题",fg="white",bg="blue")
label1.pack(anchor=NW,padx=5)
label2 = Label(win)
label2.config(text="标签内容",fg="white",bg="grey")    #配置文本属性
label2.pack(expand=YES,fill=BOTH,padx=5)
btn= Button()
btn['text']="click"                  #配置文本属性的另一种方法
btn.pack()
win.title("Example9-5")    #title()方法
win.geometry("300x200")    #geometry()方法
win.mainloop()
