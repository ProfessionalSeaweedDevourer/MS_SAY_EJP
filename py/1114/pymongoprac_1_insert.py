# 임포트
from pymongo import MongoClient

# MongoDB 연결
con = MongoClient("195.168.9.106")
db = con.nov14_student

# 데이터 입력: mongodb는 JSON 형태로 데이터를 저장. 파이썬의 딕셔너리 형태와 유사
# pymongo: mongodb 명령어를 거의 그대로 사용 가능
name = input("이름: ")
age = int(input("나이: "))

# 데이터 삽입
result = db.nov14_student.insert_one({"s_name": name, "s_age": age})

if result.acknowledged:
    print("데이터 삽입 성공")

# 연결 종료
con.close()