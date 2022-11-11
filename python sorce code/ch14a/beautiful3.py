from urllib import request
from bs4 import BeautifulSoup

response = request.urlopen("http://localhost/page1.html")
html = response.read()
html = html.decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

##print(soup.title)
##print(soup.head)
##print(soup.h3)
##print(soup.p)

##print(soup.title.string)
##for child in soup.body.children:
##    print(child)

##for child in soup.descendants:
##    print(child)
##    print("-----------------")
##
##print(soup.title.string)
##for s in soup.body.strings:
##    print(repr(s))

##temp=soup.strong
##print(temp.parent.parent)

temp2 = soup.h3
##print(temp2.next_sibling)

##for temp in temp2.next_siblings:
##    print(temp)


##lst=soup.find_all('p')
##print(lst)

##import re
##for tag in soup.find_all(re.compile('^h')):
##    print(tag.name)
##
##v1=soup.find_all('p',id='p1')
##print(v1)


print(soup.select("#p2"))
