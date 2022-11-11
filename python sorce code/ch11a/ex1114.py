# program0914.py
from tkinter import *
win =Tk()
label1=Label(win,text='Checkbutton按钮测试')
label1.config(font=('宋体',18),justify=CENTER)
label1.grid(row=1,column=1,columnspan=2)
choice1=IntVar()
choice1.set(0)
choice2=IntVar()
choice2.set(0)
frame1=Frame(bd=0,relief=RIDGE)
frame1.grid(row=2,column=1)
check1=Checkbutton(frame1,text='粗体',variable=choice1,width=8,pady=10)
check1.grid(row=1,column=1)
check2=Checkbutton(frame1,text='斜体',variable=choice2,width=8)
check2.grid(row=1,column=2)
def changeFont():
    #temp=choice1.get()
    if choice1.get()==1 and choice2.get()==1:
        label1.config(font=('宋体',18,"bold italic"))
    elif choice1.get()==1 and choice2.get()==0:
        label1.config(font=('宋体',18,"bold"))
    elif choice1.get()==0 and choice2.get()==1:
        label1.config(font=('宋体',18,"italic"))
    else:
        label1.config(font=('宋体',18))      
check1.config(command=changeFont)
check2.config(command=changeFont)
win.geometry("240x150")
mainloop()
