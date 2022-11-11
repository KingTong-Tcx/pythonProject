#program0721.py
from datetime import date,datetime
import pickle

def savedata():
    '''
    使用字典保存模块名称，创建时间和模块功能等信息，
    使用列表保存多个模块信息。
    '''
    modules=[]
    m1={"name":"登录注册","描述":'使用字典保存模块名称，创建时间和模块功能信息'}
    m2={"name":"订单管理","日期":date(2017,10,12),"描述":'订单管理模块实现的是订单数据的输入、追加、修改和删除等功能'}
    m3={"name":"客户管理","日期":datetime.now(),"描述":'使用字典保存模块名称，创建时间和模块功能信息'}     

    modules.append(m1)
    modules.append(m2)
    modules.append(m3)
        
    file=open("minfo.data", "ab")
    pickle.dump(modules,file)
    file.close()
    print("数据写入成功\n")

    file=open("minfo.data", "rb")
    lst1=pickle.load(file)
    for item in lst1:
        print(item)
    file.close()
    print("\n数据读取结束")
   
savedata()    #调用函数数
