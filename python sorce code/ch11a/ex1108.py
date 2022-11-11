# progarm0908.py
from tkinter import *

win = Tk()
frma = Frame()  # 框架frma
frmb = Frame()  # 框架frmb
frma.pack()
frmb.pack()
lblUname = Label(frma, text="UserName", width=10, fg="black")
etyUname = Entry(frma, width=20)
lblUname.grid(row=1, column=1)
etyUname.grid(row=1, column=2)
lblPwd = Label(frma, text="PassWord", width=10, fg="black")
etyPwd = Entry(frma, width=20)
lblPwd.grid(row=2, column=1)
etyPwd.grid(row=2, column=2)
# 向容器中用grid()方法添加两个按钮
btnReset = Button(frmb, text="ReSet", width=10)
btnSubmit = Button(frmb, text="Submit", width=10)
btnReset.grid(row=1, column=1)
btnSubmit.grid(row=1, column=2)
win.title("Example9-8")
win.geometry("300x200")
win.mainloop()
