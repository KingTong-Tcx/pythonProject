# ex1104.py
from tkinter import *

win = Tk()
label1 = Label(win, text="Top标签", fg="white", bg="blue")
label2 = Label(win, text="Left标签", fg="white", bg="blue")
label3 = Label(win, text="Bottom标签", fg="white", bg="blue")
label4 = Label(win, text="Right标签", fg="white", bg="blue")
label1.pack(side=TOP)
label2.pack(side=LEFT)
label3.pack(side=BOTTOM)
label4.pack(side=RIGHT)
win.title("pack()方法")  # title()方法
win.geometry("200x150")  # geometry()方法
win.mainloop()
