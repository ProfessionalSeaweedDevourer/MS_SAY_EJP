from http.client import HTTPSConnection
from bs4 import BeautifulSoup
from pymongo import MongoClient

# 1. 크롤링 및 데이터 추출
hc = HTTPSConnection("news.naver.com")
hc.request("GET", "/")
resBody = hc.getresponse().read()
hc.close()

# HTML 파싱 - BeautifulSoup
newsData = BeautifulSoup(resBody, "html.parser", from_encoding="utf-8")

# CSS 선택자 문법: '.cnf_news' 클래스를 가진 모든 요소를 선택
news_elements = newsData.select(".cnf_news")

# 추출된 텍스트 데이터를 저장할 리스트 생성
data_list = []
for n in news_elements:
    # 추출된 텍스트를 리스트에 딕셔너리 형태로 저장
    news_item = {"title": n.text.strip()}
    data_list.append(news_item)
    print(news_item) # 콘솔 출력 확인

# ----------------- 이상의 데이터를 DB에 저장 -----------------#

# 2. MongoDB 연결 및 데이터 삽입
try:
    # MongoClient 연결 (포트 번호는 기본값 27017 가정)
    con = MongoClient("195.168.9.145", 27017)
    
    # 데이터베이스 선택 (navernews DB)
    db = con.navernews
    
    # 컬렉션 선택 (navernews 컬렉션)
    collection = db.navernews
    
    # 추출된 데이터 리스트가 비어있지 않은 경우에만 삽입 진행
    if data_list:
        # insert_many()를 사용하여 리스트에 있는 모든 딕셔너리 객체를 삽입
        result = collection.insert_many(data_list) 

        if result.acknowledged:
            print(f"\n데이터 삽입 성공: 총 {len(result.inserted_ids)}개 항목")
        else:
            print("\n데이터 삽입 실패: Acknowledged가 False입니다.")
    else:
        print("\n삽입할 크롤링 데이터가 없습니다.")

except Exception as e:
    print(f"\nMongoDB 연결 또는 삽입 중 오류 발생: {e}")

finally:
    # 연결 종료
    if 'con' in locals() and con:
        con.close()
        print("MongoDB 연결 종료.")