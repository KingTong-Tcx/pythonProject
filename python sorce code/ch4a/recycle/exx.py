from urllib import request
from bs4 import BeautifulSoup

response = request.urlopen("http://www.baidu.com ")
html = response.read()
html = html.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())
