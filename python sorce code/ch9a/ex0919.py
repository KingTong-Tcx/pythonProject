# program0719.py
filename = input("请输入要添加行号的文件名：")
filename2 = input("请输入新生成的文件名：")
sourcefile = open(filename, 'r', encoding="utf-8")
targetfile = open(filename2, 'w', encoding="utf-8")
linenumber = ""
for (num, value) in enumerate(sourcefile):
    if num < 9:
        linenumber = '0' + str(num + 1)
    else:
        linenumber = str(num + 1)
    str1 = linenumber + "   " + value
    print(str1)
    targetfile.write(str1)
sourcefile.close()
targetfile.close()
