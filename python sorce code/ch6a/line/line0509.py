
 1   #program0509.py
 2   def showmessage(name, *p_info):
 3      print ("姓名: ",name)
 4      for e in p_info:
 5         print(e,end=",")
 6      return
 7    
 8   #调用showmessage函数
 9   showmessage("Kate" )
10   print ("------------------------")
11   showmessage("Kate","male",18,"Dalian")
