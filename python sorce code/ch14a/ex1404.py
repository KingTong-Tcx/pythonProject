# program1223.py
from bs4 import BeautifulSoup

doc = [
    '<!DOCTYPE html>',
    '<head>    <meta charset="UTF-8"></head>',
    '<body>',
    '<h3>段落标记的使用</h3>',
    '<hr/><p id="p1">段落标记是文档结构描述的重要元素</p>',
    '<p>&nbsp;&nbsp;段落标记实现了文本的换行显示，并且，段落之间有一行的间距。<br/>',
    '段落标记虽然有开始和结束标记，但结束标记可以省略，如果浏览器遇到一个新的段落标记，将会结束前面的段落，开始新的段落……</p>'
    , '</body>'
]
soup = BeautifulSoup("".join(doc), "html.parser")
print("-----------------网页元素信息--------------------")
print("soup.title:", soup.title)
print("soup.head:", soup.head)
print("-----------------格式化后的网页代码--------------------")
print(soup.prettify())
