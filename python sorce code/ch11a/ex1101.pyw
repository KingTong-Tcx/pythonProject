#progarm0901.py
import tkinter                           #导入tkinter模块
win = tkinter.Tk()                      #创建窗口对象
label1 = tkinter.Label(win,text="Hello,Python")   #创建标签对象
btn1 = tkinter.Button(win,text="click")             #创建按钮对象
label1.pack()       #打包对象，使其显示在其父容器中
btn1.pack()
win.mainloop()      #启动事件循环
