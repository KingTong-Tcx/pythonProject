
 1   #program0508.py
 2   
 3   def showmessage(name,age=18):
 4      "打印任何传入的字符串"
 5      print ("姓名: ",name)
 6      print ("年龄: ",age)
 7      return
 8    
 9   #调用showmessage函数
10   showmessage(age=19,name="Kate" )
11   print ("------------------------")
12   showmessage(name="John")
