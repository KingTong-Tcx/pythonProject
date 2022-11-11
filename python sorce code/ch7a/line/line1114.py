
 1   #program1114.py
 2   class Phone:                  #电话类
 3       def receive(self):
 4           print("接电话")
 5       def send(self):
 6            print("打电话")
 7   
 8   class Message:	               #消息类
 9       def reveiveMsg(self):
10           print("接收短信") 
11       def sendMsg(self):
12           print("发送短信")
13   
14   class Mobile(Phone,Message):   #手机类
15       pass
16   
17   mobile=Mobile()
18   mobile.receive()
19   mobile.send()
20   mobile.reveiveMsg()
21   mobile.sendMsg()
