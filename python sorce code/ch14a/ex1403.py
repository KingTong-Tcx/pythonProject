#program1222.py
import requests

def getHTMLText():
    r=requests.get(url,timeout=15)
    r.raise_for_status()
    r.encoding='utf-8'    #如果中文字符是否能正常显示，更改编码方式为utf-8
    return r.text[:200]

url = "http://www.sohu.com"
text=getHTMLText()
print(text)
