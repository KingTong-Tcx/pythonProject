# program1221.py
import urllib.request

fopen = urllib.request.urlopen("http://www.sohu.com")
print("Status:", fopen.status, fopen.reason)
print("-----------以下HTTP响应头信息---------")
for k, v in fopen.getheaders():
    print("%s:%s" % (k, v))
fopen.close()
