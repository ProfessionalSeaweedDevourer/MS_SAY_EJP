from pymongo import MongoClient

con = MongoClient("195.168.9.244")
db = con.kwon

f = open("C:/Kwon/naverNews.txt", "a", encoding="utf-8")

news = db.naverNews.find()
for n in news:
    f.write("%s\n" % n["txt"])

f.close()
con.close()
