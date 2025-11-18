from http.client import HTTPSConnection
from bs4 import BeautifulSoup
from pymongo import MongoClient

# 1. 접속 정보 변경: 멜론 차트 주소로 변경해야 합니다.
# 실제 멜론 차트의 HOST와 PATH로 변경해야 합니다.
# 예시: 멜론 메인 페이지 또는 특정 차트 페이지
HOST = "www.melon.com" 
PATH = "/chart" 

# 2. 크롤링 실행 및 User-Agent 헤더 추가 (접속 차단 방지 시도)
try:
    hc = HTTPSConnection(HOST)
    # 중요: User-Agent 헤더를 추가하여 봇이 아닌 일반 웹 브라우저처럼 보이게 합니다.
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    hc.request("GET", PATH, headers=headers)
    resBody = hc.getresponse().read()
    hc.close()

# 그 외의 문제: 스크롤이 바닥에 닿아야 추가 데이터가 로드되는 경우,
# 또는 JavaScript로 동적으로 생성되는 콘텐츠인 경우.
# >> 매크로를 만들어서 무식하게 해결...또는 Selenium 같은 도구 사용.

except Exception as e:
    print(f"웹 접속 오류 발생: {e}")
    resBody = b""

# 3. MongoDB 연결 및 DB/컬렉션 설정
con = MongoClient("195.168.9.145")
db = con.melon_chart
chart_collection = db.tracks

# 4. 파싱 및 데이터 추출
chartData = BeautifulSoup(resBody, "html.parser", from_encoding="utf-8")

track_elements = chartData.select('a[title*="재생"]') 

if track_elements:
    print(f"총 {len(track_elements)}개의 트랙 요소를 찾았습니다.")
    
    for track in track_elements:
        track_name = track.text.strip()
        
        # 텍스트 내용이 'Blue Valentine'과 같이 곡명임을 확인합니다.
        if track_name: 
            chart_collection.insert_one({"track_name": track_name})
            
    print("멜론 차트 곡명이 성공적으로 MongoDB에 저장되었습니다.")
else:
    print("경고: 지정된 선택자로 곡명 요소를 찾지 못했습니다. 멜론 차트 HTML 구조를 다시 확인해 주세요.")

con.close()