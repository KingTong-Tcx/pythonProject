
 1   #program0510.py
 2   def showmessage(name,*p_info,**scores):
 3      print ("姓名: ",name)
 4      for e in p_info:
 5         print(e,end=" ")
 6      for item in scores.items():
 7         print(item,end=" ")
 8      print()   
 9      return
10    
11   #调用showmessage函数
12   showmessage("Kate","male",18,"Dalian");
13   print("------------------------------")
14   showmessage("Kate","male",18,"Dalian",math=86,pe=92,eng=88)
