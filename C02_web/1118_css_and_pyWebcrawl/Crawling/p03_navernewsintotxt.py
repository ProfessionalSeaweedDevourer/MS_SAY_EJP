from pymongo import MongoClient

con = MongoClient("195.168.9.145")
db = con.navernews

f = open("C:/Users/soldesk/NaverNews.txt", "a", encoding="utf-8")

news = db.navernews.find()
for n in news:
    f.write("%s\n" % n["txt"])

f.close()
con.close()