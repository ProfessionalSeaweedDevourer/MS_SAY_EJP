# 멜론 : 데이터는 주고싶지않고, 일반 사용자들 차트나 보여주겠다
# 우리 : 차트 보여준다 -> 데이터 주겠다는거 아닌가?

# 1) 정식으로 웹브라우저 켜서 웹사이트 접속은 가능, 프로그램 만들어서 GET방식 요청은 막아놓은 사이트가 많음
# 2) 일단 10개 나옴 -> 스크롤시켜서 바닥에 닿으면 다음 10개 나오고 -> 스크롤은 뭘로?
# 
# -> 매크로를 만들자(웹브라우저 켜서, 접속하고, 스크롤시키고, 웹브라우저의 데이터 받아오는)

# selenium
#   Python HTML 파싱 라이브러리
#   웹브라우저 매크로 라이브러리
#
# 시작 - cmd
#   pip install selenium

# 따로 브라우저용 드라이버가 필요했었는데
# 최신버전 selenium은 포함되어있음
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.melon.com/chart/index.htm")

# driver.execute_script("JavaScript소스")
_as = driver.find_elements(By.CSS_SELECTOR, ".rank01 span a")
for a in _as:
    print(a.text)