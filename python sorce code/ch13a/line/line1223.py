1  # program1223.py
2
from bs4 import BeautifulSoup

3
doc = [
    4   '<!DOCTYPE html>',
    5   '<head>    <meta charset="UTF-8"></head>',
    6   '<body>',
    7   '<h3>段落标记的使用</h3>',
    8   '<hr/><p id="p1">段落标记是文档结构描述的重要元素</p>',
    9   '<p>&nbsp;&nbsp;段落标记实现了文本的换行显示，并且，段落之间有一行的间距。<br/>',
    10      '段落标记虽然有开始和结束标记，但结束标记可以省略，如果浏览器遇到一个新的段落标记，将会结束前面的段落，开始新的段落……</p>'
    11, '</body>'
    12]
13
soup = BeautifulSoup("".join(doc), "html.parser")
14
print("-----------------网页元素信息--------------------")
15
print("soup.title:", soup.title)
16
print("soup.head:", soup.head)
17
print("-----------------格式化后的网页代码--------------------")
18
print(soup.prettify())
