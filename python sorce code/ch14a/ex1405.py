# ex1405.py
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    r.encoding = 'utf-8'  # 如果中文字符是否能正常显示，更改编码方式为utf-8
    # print(text)
    return r.text


def getSoup(url):
    txt = getHTMLText(url)
    soup = BeautifulSoup(txt, "html.parser")
    return soup


def getContent(soup):
    contents = soup.find('div', {'class': 'usoft-listview-basic'})
    articles = []
    for item in contents.find_all('li'):
        date1 = item.find('span', {'class': 'usoft-listview-item-date'})
        datestr = date1.string
        title = item.find('a')['title']
        # hrefstr=item.string
        articles.append([title, "----", datestr])
        # print(datestr,'-----',title)
    return articles


if __name__ == "__main__":
    url = "http://www.upln.cn/html/Channel_01/Column_0103/"
    soup = getSoup(url)
    articlelist = getContent(soup)
    # 显示爬取信息
    for item in articlelist:
        for i in item:
            print(i, end=" ")
        print()
        print('----------------------------------------------------------')
