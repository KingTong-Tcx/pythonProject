# program1220.py
import urllib.request
fopen=urllib.request.urlopen("http://www.sohu.com")
html=fopen.read(360)
print(html)
print(html.decode("utf-8"))
fopen.close()
