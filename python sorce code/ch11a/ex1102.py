#ex1102.py
from tkinter import *
win=Tk()
label = Label(win,text="Hello,Python")
btn1= Button(win,text="click")
label.pack()
btn1.pack()
win.title("Example11-2")     #title()方法
win.geometry("300x200")     #geometry()方法
win.mainloop()
