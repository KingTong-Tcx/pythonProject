# program0915.py
from tkinter import *
win=Tk()

frame1=LabelFrame(relief=GROOVE,text='工具栏：')
frame1.pack(anchor=NW,fill=X)
bt1=Button(frame1,text='复制')
bt1.grid(row=1,column=1)
bt2=Button(frame1,text='剪切')
bt2.grid(row=1,column=2)
bt3=Button(frame1,text='粘贴')
bt3.grid(row=1,column=3)

text1=Text()
text1.pack(expand=YES,fill=BOTH)

def docopy():
    data=text1.get(SEL_FIRST,SEL_LAST)  #获得选中内容    
    text1.clipboard_clear()             #清除剪贴板
    text1.clipboard_append(data)        #将内容写入剪贴板	
def docut():    
    data=text1.get(SEL_FIRST,SEL_LAST)
    text1.delete(SEL_FIRST,SEL_LAST)    #删除选中内容  	
    text1.clipboard_clear()
    text1.clipboard_append(data)
def dopaste():
    text1.insert(INSERT,text1.clipboard_get())  #插入剪贴板内容
def doclear():
    text1.delete('1.0',END)         	    	#删除全部内容

bt1.config(command=docopy)
bt2.config(command=docut)
bt3.config(command=dopaste)

mainloop()
