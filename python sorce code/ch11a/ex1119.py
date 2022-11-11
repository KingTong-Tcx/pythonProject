#ex1119.py
import tkinter
import tkinter.messagebox
import tkinter.ttk

#创建tkinter应用程序
win = tkinter.Tk()
#设置窗口标题
win.title('考试系统注册')
#定义窗口大小
win.geometry("440x360")
#与姓名关联的变量
varName = tkinter.StringVar()
varName.set('')
#创建标签，然后放到窗口上
labelName=tkinter.Label(win, text='学生姓名:',justify=tkinter.LEFT,width=10)
labelName.grid(row=1,column=1)
#创建文本框，同时设置关联的变量
entryName = tkinter.Entry(win, width=14,textvariable=varName)
entryName.grid(row=1,column=2,pady=5)

labelGrade=tkinter.Label(win,text='省份：',justify=tkinter.RIGHT,width=10)
labelGrade.grid(row=3,column=1)

#模拟考生所在地区，字典键为省份，字典值为地区
datas = {'辽宁省':['沈阳市', '大连市', '鞍山市', '抚顺市'],
               '吉林省':['长春市', '吉林市','白山市'],
               '黑龙江省':['哈尔滨市', '大庆市', '牡丹江市']}
#考生省份组合框
comboPrvince=tkinter.ttk.Combobox(win,width=11,values=tuple(datas.keys()))
comboPrvince.grid(row=3,column=2)
#事件处理函数
def comboChange(event):
    grade = comboPrvince.get()
    if grade:
        #动态改变组合框可选项
        comboCity["values"] = datas.get(grade)
    else:
        comboCity.set([])
        
#绑定组合框事件处理函数
comboPrvince.bind('<<ComboboxSelected>>', comboChange)

labelClass=tkinter.Label(win,text='地区:',justify=tkinter.RIGHT,width=10)
labelClass.grid(row=3,column=3)
#考生地区组合框
comboCity = tkinter.ttk.Combobox(win, width=11)
comboCity.grid(row=3,column=4)

labelSex=tkinter.Label(win,text='请选择类别:',justify=tkinter.RIGHT,width=10)
labelSex.grid(row=5,column=1)


#与考生类别关联的变量，1:本科学生；0:专科学生，默认为本科学生
stuType = tkinter.IntVar()
stuType.set(1)
radio1=tkinter.Radiobutton(win,variable=stuType,value=1,text='本科学生')
radio1.grid(row=5,column=2,pady=5)
radio2=tkinter.Radiobutton(win,variable=stuType,value=0,text='专科学生')
radio2.grid(row=5,column=3)

#与是否英语专业关联的变量
major = tkinter.IntVar()
major.set(0)
#复选框，选中时变量值为1，#未选中时变量值为0
checkmajor=tkinter.Checkbutton(win,text='是否英语专业?',/
                                 variable=major,onvalue=1,offvalue=0)
checkmajor.grid(row=7,column=1,pady=5)

#添加按钮单击事件处理函数
def addInformation():
    result= ' 学生姓名:' + entryName.get()
    result= result+ '; 省份:' + comboPrvince.get()
    result= result+ '; 地区:' + comboCity.get()
    result= result+ '; 类别:'+('本科学生' if stuType.get() else '专科学生')
    result= result+ '; 英语专业:' + ('Yes' if major.get() else 'No')
    listboxStudents.insert(0, result)
    
buttonAdd= tkinter.Button(win,text='增加',width=10,command=addInformation)
buttonAdd.grid(row=7,column=2)

#删除按钮的事件处理函数
def deleteSelection():
    selection = listboxStudents.curselection()
    if  not selection:
        tkinter.messagebox.showinfo(title='Information', message='No Selection')
    else:
        listboxStudents.delete(selection)
        
buttonDelete= tkinter.Button(win, text='删除',width=10,command=deleteSelection)
buttonDelete.grid(row=7,column=3)
#创建列表框组件
listboxStudents = tkinter.Listbox(win, width=60)
listboxStudents.grid(row=8,column=1,columnspan=4,padx=5)
#启动消息循环
win.mainloop()
