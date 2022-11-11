# program0508.py

def showmessage(name, age=18):
    "打印任何传入的字符串"
    print("姓名: ", name)
    print("年龄: ", age)
    return


# 调用showmessage函数
showmessage(age=19, name="Kate")
print("------------------------")
showmessage(name="John")
