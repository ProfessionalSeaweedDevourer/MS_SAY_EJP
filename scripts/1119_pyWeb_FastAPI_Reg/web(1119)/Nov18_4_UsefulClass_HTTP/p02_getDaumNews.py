from http.client import HTTPSConnection

from bs4 import BeautifulSoup

hc = HTTPSConnection("news.daum.net")
hc.request("GET", "/")
resBody = hc.getresponse().read()
hc.close()

newsData = BeautifulSoup(resBody, "html.parser", from_encoding="utf-8")
news = newsData.select(".item_newsheadline2 .cont_thumb .tit_txt")
for n in news:
    print(n.text)