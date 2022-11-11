#progarm0912.py
from tkinter import *
win=Tk()
listbox=Listbox(win)
#初始化列表框
items=["HTML5","CSS3","JavaScript","Jquery"]
for item in items:
    listbox.insert(END,item)
listbox.pack(side=LEFT,expand=1,fill=Y)
def additem():						     #在列表框中填加选项
    str=entry1.get()    
    if not str=='':
        index=listbox.curselection()
        if len(index)>0:
            listbox.insert(index[0],str)		#有选中项时，在选中项前面添加一项
        else:
            listbox.insert(END,str)			#无选中项时，添加到最后
def removeitem():					           #在列表框中删除选项
    index=listbox.curselection()
    if len(index)>0:
        if len(index)>1:
            listbox.delete(index[0],index[-1])	#删除选中的多项
        else:                
            listbox.delete(index[0])			      #删除选中的一项
entry1=Entry(width=20)
entry1.pack(anchor=NW)
bt1=Button(text='添加',command=additem)
bt1.pack(anchor=NW)
bt2=Button(text='删除',command=removeitem)
bt2.pack(anchor=NW)
mainloop()
