#program0510.py
def showmessage(name,*p_info,**scores):
   print ("姓名: ",name)
   for e in p_info:
      print(e,end=" ")
   for item in scores.items():
      print(item,end=" ")
   print()   
   return
 
#调用showmessage函数
showmessage("Kate","male",18,"Dalian");
print("------------------------------")
showmessage("Kate","male",18,"Dalian",math=86,pe=92,eng=88)
