from oracledb import connect

con = connect("ericjpark/0000@195.168.9.249:1521/xe") 

# 데이터
name = input("가격을 변경할 제품명: ")
price = int(input("수정된 가격: "))

# str 형태로 sql 작성 - ";" 빼고!
sql = "update 제품 set 제품_가격 = %d where 제품_제품명 = '%s' " % (price, name)

# # 이때 정확히 같은 것이 아니라 유사 검색을 쓰려면...
# #      > %키워드% 를 해야 하는데, 이러면 %s가 깨진다.
# # 이 경우에는...
# name = "%" + name + "%" # 이렇게 처리해서 입력값에 앞뒤로 %를 붙이자.
# sql += " update 제품 set 제품_가격 = %d where 제품_제품명 like '%s' " % (price, name)

print(sql)


# 작성된 구문을 전송 - 실행 - 결과 받아오기...를 해 주는 함수 딸깍
cur = con.cursor()
cur.execute(sql)

# 결과 확인
if cur.rowcount == 1:
    print("변경 성공.")
    con.commit()
else:
    print("변경 실패.")

cur.close()
# * commit은 수동으로 해 줘야 함.

# 연결해제
con.close()