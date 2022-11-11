from bs4 import BeautifulSoup
soup=BeautifulSoup(open("page1.html", 'r', encoding="utf-8"), "html.parser") #提供本地HTML文件
print(soup.head)
print(soup.a)
                   
