#progarm0911.py
from tkinter import *
def computing():
    sum = 0
    n= int(number.get())
    for i in range(n+1):
        sum+=i
    result="累加结果是："+ str(sum)
    label3.config(text=result)
win=Tk()
win.title("Entry Test")
win.geometry("300x200")
label1=Label(win,text='请输入计算数据： ')
label1.config(width=16,height=3)
label1.config(font=('宋体',12))
label1.grid(row=0,column=0)
number = StringVar()
entry1 = Entry(win,textvariable = number,width=16)
entry1.grid(row=0,column=1)
label2=Label(win,text='请单击确认：')
label2.config(width=14,height=3)
label2.config(font=('宋体',12))
label2.grid(row=1,column=0)
button1=Button(win,text="计算")	
button1.config(justify=CENTER)			#设置按钮文本居中
button1.config(width=14,height=2)		#设置按钮的宽和高
button1.config(bd=3,relief=RAISED)		#设置边框宽度和样式
button1.config(anchor=CENTER)			#设置内容在按钮内部居中
button1.config(font=('隶书',12))		
button1.config(command=computing)
button1.grid(row=1,column=1)
label3=Label(win,text='显示结果 ')
label3.config(width=16,height=3)
label3.config(font=('宋体',12))
label3.place(x=50,y=130)
win.mainloop()
