# program0918.py
from tkinter import *
def leftkey(event):
    label1.config(text="单击左键")
def rightkey(event):
    label1.config(text="单击右键")
def returnkey(event):
    label1.config(text="按回车键")
def mousemove(event):
    temp="鼠标位置:{},{}".format(event.x,event.y)
    label1.config(text=temp)  
def keypress(event):
    temp="按键是{}".format(event.char)
    label1.config(text=temp) 
win=Tk()
label1=Label(text='测试显示结果',font=("黑体",14),fg="blue")
label2=Label(text='常用事件测试',justify=CENTER,font=("楷体",18))
label1.pack()
label2.pack()
label2.focus()          #焦点置于label2用于测试Return、KeyPress事件。
label2.bind("<Button-1>",leftkey)
label2.bind("<3>",rightkey)             #label2.bind("<Button-3>",rightkey)
label2.bind("<Return>",returnkey)
label2.bind("<B1-Motion>",mousemove)   #拖动事件
label2.bind("<KeyPress>",keypress)     #按键事件
win.geometry("300x200")
win.mainloop()

