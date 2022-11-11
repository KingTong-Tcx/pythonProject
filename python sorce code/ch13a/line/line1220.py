 1   # program1220.py
 2   import urllib.request
 3   fopen=urllib.request.urlopen("http://www.sohu.com")
 4   html=fopen.read(360)
 5   print(html)
 6   print(html.decode("utf-8"))
 7   fopen.close()
