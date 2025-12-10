from oracledb import connect

con = connect("ericjpark/0000@195.168.9.249:1521/xe") 

# 데이터
name = input("사명: ")

# str 형태로 sql 작성 - ";" 빼고!
sql = "delete from 회사 where 회사_사명 = '%s'" % name
print(sql)

# 작성된 구문을 전송 - 실행 - 결과 받아오기...를 해 주는 함수 딸깍
cur = con.cursor()
cur.execute(sql)

# 결과 확인
if cur.rowcount == 1:
    print("삭제 성공.")
    con.commit()
else:
    print("삭제 실패.")

cur.close()
# * commit은 수동으로 해 줘야 함.

# 연결해제
con.close()