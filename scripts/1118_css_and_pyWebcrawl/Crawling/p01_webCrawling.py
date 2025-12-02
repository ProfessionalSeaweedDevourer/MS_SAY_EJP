# web crawling: 현실적으로 생각하면 html 문서를 가져오는 방법
# XML: 데이터를 HTML DOM 꼴로 표현한 것
# JSON: 데이터를 JSON 배열+객체 꼴로 표현한 것
# HTML: ???
#     > 애초에 HTML 문서는 사람이 읽기 위한 문서이지, 데이터를 주고받기 위한 문서가 아님
#     > 법적인 문제도...

from http.client import HTTPConnection

hc = HTTPConnection("news.daum.net")
hc.request("GET", "/")
resBody = hc.getresponse().read()
hc.close()

# html 파싱 - BeautifulSoup
from bs4 import BeautifulSoup

newsData = BeautifulSoup(resBody, "html.parser", from_encoding="utf-8")
news = newsData.select(".item_newsheadline2 .cont_thumb .tit_txt")  # CSS 선택자 문법
for n in news:
    print(n.text)

# 대상 웹사이트에서 '어떤 부분'이 각 뉴스 제목을 가리키는지 찾아서 긁어오기