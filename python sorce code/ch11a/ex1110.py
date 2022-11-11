#progarm0910.py
from tkinter import *
win=Tk()
win.title("Button Test")
win.geometry("300x200")
label1=Label(win,text='此处显示计算结果 ')
label1.config(font=('宋体',12))
label1.pack()
def computing():
    sum = 0
    for i in range(100+1):
        sum+=i
    result="累加结果是："+ str(sum)
    label1.config(text=result)  
str1='计算1-100累加值'
mybutton=Button(win,text=str1)	
mybutton.config(justify=CENTER)		#设置按钮文本居中
mybutton.config(width=20,height=3)		#设置标签的宽和高
mybutton.config(bd=3,relief=RAISED)	#设置边框宽度和样式
mybutton.config(anchor=CENTER)			#设置内容在按钮内部居中
mybutton.config(font=('隶书',12,'underline'))		
mybutton.config(command=computing)
mybutton.config(activebackground='yellow')
mybutton.config(activeforeground='red')
mybutton.pack()
win.mainloop()
