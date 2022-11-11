#progarm0907.py
from tkinter import *
win=Tk()
label1 = Label(win,text="place()方法测试",fg="black")
label1.place(x=140,y=50,anchor=N)    #place()方法布局
btn1= Button(text="place()按钮")
btn2= Button(text="grid()")
btn1.place(x=140,y=80,anchor=N)      #place()方法布局
btn2.grid(row=2,column=1)            #grid()方法布局
win.title("Example9-7") 
win.geometry ("300x200")
win.mainloop()
