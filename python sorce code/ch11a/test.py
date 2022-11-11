users={"zhang3":"a12","admin":"123456","li4":"abc"}
name="admin"
pwd="1256"
flag=False
for item in users:
    if item==name and users[item]==pwd:
        flag=True

if flag==True:
    print(1111)
else:
    print(0)
  
