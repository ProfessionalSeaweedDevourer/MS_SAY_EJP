# 기본 포트 번호: http 80, https 443

from http.client import HTTPSConnection

hc = HTTPSConnection("www.kma.go.kr") # '대상 폴더' 직전까지의 도메인, 또는 ip, 포트 등

hc.request("GET", "/repository/xml/fct/mon/img/fct_mon1rss_108_20251030.xml")

res = hc.getresponse()
resBody = res.read()
print(resBody.decode())

hc.close() # 따로 하지 않아도 기본 30분 후 세션 종료.