# program0916.py
from tkinter import *
win=Tk()
win.geometry("300x200")     #geometry()方法
label1=Label(text='请选择评语和成绩')
label1.pack(expand=1,fill=X)
label1.config(font=('隶书',15))
label2=Label()
label2.config(font=('宋体',18))
label2.pack()
subject=StringVar()
score=IntVar()
spin1=Spinbox(textvariable=subject,value=('语文','数学','外语'),wrap=True)
spin1.pack()
spin2=Spinbox(textvariable=score,from_=60,to=100,increment=5,wrap=True)
spin2.pack()
def change():
    label2.config(text=subject.get()+str(score.get()))
button1=Button(text="确定",command=change)
button1.pack()
win.mainloop()
