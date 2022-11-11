#progarm0913.py
from tkinter import *

win =Tk()
label1=Label(win,text='请为您最喜欢的体育项目投票')
label1.grid(row=1,column=1,columnspan=2)

s_items=IntVar()
s_items.set(2)

frame1=Frame(bd=2,relief=RIDGE)
frame1.grid(row=2,column=1)

frame2=Frame(bd=0,relief=RIDGE)
frame2.grid(row=2,column=2)

radio1=Radiobutton(frame1,text='足球',variable=s_items,value=1,width=8)
radio1.grid(row=1,column=1)
radio2=Radiobutton(frame1,text='排球',variable=s_items,value=2)
radio2.grid(row=2,column=1)
radio3=Radiobutton(frame1,text='篮球',variable=s_items,value=3)
radio3.grid(row=3,column=1)

num1=IntVar()
entry1 = Entry(frame2,textvariable=num1,width=10,state = 'readonly')
entry1.grid(row=1,column=1,pady=4)
num2=IntVar()
entry2 = Entry(frame2,textvariable=num2,width=10,state = 'readonly')
entry2.grid(row=2,column=1,pady=4)
num3=IntVar()
entry3 = Entry(frame2,textvariable=num3,width=10,state = 'readonly')
entry3.grid(row=3,column=1,pady=4)

def voting():
    global num1,num2,num3
    temp=s_items.get()
    if temp==2:
        num2.set(num2.get()+1)
    elif temp==1:
        num1.set(num1.get()+1)
    else:
        num3.set(num3.get()+1)

btn1=Button(win,text="请投票",command=voting)
btn1.grid(row=3,column=1,columnspan=2,pady=5)

win.geometry("300x200")
mainloop()
