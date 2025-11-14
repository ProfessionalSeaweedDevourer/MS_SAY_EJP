# 임포트
import re
from pymongo import ASCENDING, DESCENDING, MongoClient

# MongoDB 연결
con = MongoClient("195.168.9.106")
db = con.nov14_student

# 데이터 삽입
# 이때, pymongo에서의 sort는 딕셔너리-튜플 형태로 정렬 기준을 지정
# db.컬렉션.find().sort({필드명:1 or -1})
result = db.nov14_student.find().sort([("s_name", ASCENDING), ("s_age", DESCENDING)])

for s in result:
    print(f"이름: {s['s_name']}, 나이: {s['s_age']}")
    print("-" * 30)

# 연결 종료
con.close()