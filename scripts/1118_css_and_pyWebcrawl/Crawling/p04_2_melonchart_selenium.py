from http.client import HTTPSConnection
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() 
driver.get(f"https://www.melon.com/chart")

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# ...는 JS를 배워야 쓸 수 있음

_as = driver.find_element(By.CSS_SELECTOR, ".rank01 span a")  # 멜론 차트 곡명 선택자
# 실제 이 스크립트를 쓰지는 않겠지만, CSS 선택자 연습의 일환
for a in _as:
    print(a.text)
