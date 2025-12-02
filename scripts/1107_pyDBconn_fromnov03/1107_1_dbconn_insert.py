# '통신'에 대해: socket의 실시간 통신, http의 비-실시간 통신.
# db 서버와 외부 스크립트 간의 상호작용도 '통신'이다.
# 그런데, db 종류에 따라 통신 방식이 다르다. > 표준 '프로토콜'이 없다.
# > 남이 만들어 준 것을 활용.

# * 구버전 db의 경우 ic가 따로 필요

# oracledb.py 활용
from oracledb import connect

# 등록

# 연결 

con = connect("ericjpark/0000@195.168.9.249:1521/xe") 
# 여기는 sqlplus 클라이언트처럼 접속

# 데이터
name = input("사명: ")
addr = input("주소: ")
ceo = input("사장: ")
emp = int(input("직원 수: "))

# str 형태로 sql 작성 - ";" 빼고!
sql = "insert into 회사 values('%s', '%s', '%s', %d)" % (name, addr, ceo, emp)
print(sql)

# 작성된 구문을 전송 - 실행 - 결과 받아오기...를 해 주는 함수 딸깍
cur = con.cursor()
cur.execute(sql)

# 결과 확인
if cur.rowcount == 1:
    print("등록 성공.")
    con.commit()
else:
    print("등록 실패.")

cur.close()
# * commit은 수동으로 해 줘야 함.

# 연결해제
con.close()