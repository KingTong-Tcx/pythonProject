# ex1406.py
import requests
import time
from bs4 import BeautifulSoup


# 爬取网页页面内容
def getHTMLText(path):
    r = requests.get(path, timeout=15)
    r.raise_for_status()
    r.encoding = 'utf-8'  # 如果中文字符是否能正常显示，更改编码方式为utf-8
    # print(text)
    return r.text


# 解析网页
def getNewsList(root, url, appointeddate):
    articles = []
    while True:
        path = root + url
        txt = getHTMLText(path)
        soup = BeautifulSoup(txt, "html.parser")
        contents = soup.find('div', {'class': 'usoft-listview-basic'})
        for item in contents.find_all('li'):
            # 解析获得日期信息
            date1 = item.find('span', {'class': 'usoft-listview-item-date'}).string
            if time.mktime(time.strptime(date1, "%Y-%m-%d")) < appointeddate:
                break
            datestr = date1.string
            title = item.find('a')['title']
            articles.append([datestr, '-----', title])

        # 信息分布在多个页面的情况
        if time.mktime(time.strptime(date1, "%Y-%m-%d")) > appointeddate:
            # 找到下一页的链接
            pages = contents.find('div', {'class': 'usoft-page-divide'})
            page = pages.find_all('a', {'class': 'a1'})[2]
            url = page['href']
        else:
            break
    return articles


if __name__ == "__main__":
    root = "http://www.upln.cn"
    url = '/html/Channel_01/Column_0103/'
    lastdate = time.mktime(time.strptime('2018-4-1', "%Y-%m-%d"))
    newslist = getNewsList(root, url, lastdate)
    if len(newslist) == 0:
        print("无满足指定日期条件信息")
    else:
        for item in newslist:
            for i in item:
                print(i, end="")
            print()
