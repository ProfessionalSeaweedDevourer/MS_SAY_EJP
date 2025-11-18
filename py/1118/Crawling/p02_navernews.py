from http.client import HTTPSConnection
from bs4 import BeautifulSoup
from pymongo import MongoClient

hc = HTTPSConnection("news.naver.com")
hc.request("GET", "/")
resBody = hc.getresponse().read()
hc.close()

con = MongoClient("195.168.9.145")
db = con.navernews

newsData = BeautifulSoup(resBody, "html.parser", from_encoding="utf-8")
news = newsData.select(".cnf_news")
for n in news:
    db.navernews.insert_one({"txt":n.text})

con.close()