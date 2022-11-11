import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    r=requests.get(url,timeout=15)
    r.raise_for_status()
    r.encoding='utf-8'    #如果中文字符是否能正常显示，更改编码方式为utf-8
    #print(text)    
    return r.text

def getSoup(url):
    txt=getHTMLText(url)
    soup=BeautifulSoup(txt,"html.parser")
    return soup
    
def getContent(soup): 
    content=soup.select('.notice')
    #print(content)
    
    for infos in content:
        info=infos.select('li')
        for i in info:
            print(type(i.a['href']))

            print(i.string)
            print("-----------------------")

url = "http://www.lnzsks.com/index.html"
#text=getHTMLText(url)
soup =getSoup(url)
getContent(soup)
