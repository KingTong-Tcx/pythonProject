#program0509.py
def showmessage(name, *p_info):
   print ("姓名: ",name)
   for e in p_info:
      print(e,end=",")
   return
 
#调用showmessage函数
showmessage("Kate" )
print ("------------------------")
showmessage("Kate","male",18,"Dalian")
