from oracledb import connect

con = connect("ericjpark/0000@195.168.9.249:1521/xe") 

# 회사 테이블 내용 조회.
sql = "SELECT avg(제품_가격) FROM 제품"

print(sql)

# DB 작업을 진행하는 객체 / 결과 반환기 cursor 호출.
cur = con.cursor()

cur.execute(sql)
print("------")

for result in cur:
    print(f"평균 제품가: {result[0]}")

cur.close()

con.close()
