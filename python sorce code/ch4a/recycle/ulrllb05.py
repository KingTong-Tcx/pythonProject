##import urllib.request
##fp=urllib.request.urlopen("http://www.sohu.com")
##print(fp.read(100))
###print(fp.read(100).decode())
##fp.close()


import urllib.request
import urllib

data = urllib.parse.urlencode({"from": 'Beijing', "To": "Shanghai"})
url = "http://www.sohu.com"
f = urllib.request.urlopen("http://www.sohu.com%s" % data)
print(f.read(1500))
f.close()
