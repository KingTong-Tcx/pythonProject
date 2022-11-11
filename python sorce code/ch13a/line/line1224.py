1  # program1224.py
2
import requests

3
from bs4 import BeautifulSoup

4
5


def getHTMLText(url):


    6
r = requests.get(url, timeout=15)
7
r.raise_for_status()
8
r.encoding = 'utf-8'  # 如果中文字符是否能正常显示，更改编码方式为utf-8
9  # print(text)
10
return r.text
11
12


def getSoup(url):


    13
txt = getHTMLText(url)
14
soup = BeautifulSoup(txt, "html.parser")
15
return soup
16
17


def getContent(soup):


    18
contents = soup.select('.hot')
19  # print(content)   #用于测试查找到的类选择器.hot的内容
20
for items in contents:
    21
item = items.select('li')  # 遍历一条要闻
22
for i in item:
    23
strhref = i.a['href']  # 返回超级链接的属性信息
24
datastr = strhref[15:23]  # 返回要闻的发表时间
25
26  # print(i.string,datastr)
27
print("{:<36} {:<8}".format(i.string, datastr))
28
print("--------------------------------------------------------------")
29
if __name__ == "__main__":
    30
url = "http://www.lnzsks.com/index.html"
31
soup = getSoup(url)
32
getContent(soup)
