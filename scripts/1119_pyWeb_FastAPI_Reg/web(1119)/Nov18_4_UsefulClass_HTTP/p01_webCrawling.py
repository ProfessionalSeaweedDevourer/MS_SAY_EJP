# AI훈련용 데이터
#   1) 발로 뛰어서
#   2) 만들어져있는 데이터 구해서
#   3) 웹 데이터
#       XML
#       JSON
#       XML/JSON이 없으면 -> 웹사이트에서 긁어오자

# web crawling(scraping)
#   넓은의미 : 어쨌든 웹 데이터
#   진짜의미 : HTML파싱

# 근데
#   XML : 데이터를 HTML DOM객체 모양으로 표현해놓은거
#   JSON : 데이터를 JSON 배열+객체 모양으로 표현해놓은거
#   HTML : 웹사이트 만들때 쓰는 디자인 언어
#       -> 파싱 난이도가
#       -> 법적문제

from http.client import HTTPConnection

from bs4 import BeautifulSoup

hc = HTTPConnection("195.168.9.153")
hc.request("GET", "/review.html")
resBody = hc.getresponse().read()
hc.close()
############
# BeautifulSoup
#   Python HTML 파싱 라이브러리
#   시작 - cmd
#       pip install bs4
                        # 받아온거, 내장html파서이름, 인코딩방식
reviewData = BeautifulSoup(resBody, "html.parser", from_encoding="utf-8") 
reviews = reviewData.select(".aReview") # CSS선택자
for r in reviews:
    tds = r.select("td")
    print(tds[3].text)