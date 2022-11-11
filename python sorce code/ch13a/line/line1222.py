1  # program1222.py
2
import requests

3
4


def getHTMLText():


    5
r = requests.get(url, timeout=15)
6
r.raise_for_status()
7
r.encoding = 'utf-8'  # 如果中文字符是否能正常显示，更改编码方式为utf-8
8
return r.text[:200]
9
10
url = "http://www.sohu.com"
11
text = getHTMLText()
12
print(text)
