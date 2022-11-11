
 1   #program1221.py
 2   import urllib.request
 3   fopen=urllib.request.urlopen("http://www.sohu.com")
 4   print("Status:",fopen.status,fopen.reason)
 5   print("-----------以下HTTP响应头信息---------")
 6   for k,v in fopen.getheaders():
 7       print("%s:%s"%(k,v))
 8   fopen.close()
