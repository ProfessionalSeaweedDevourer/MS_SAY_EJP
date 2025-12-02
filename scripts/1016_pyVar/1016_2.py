# 변수(Variable): 데이터의 임시 저장소
# 기존 python 문법, 숫자로 시작하는 변수명은 불가. 특수문자도 불가.

# 변수명 짓기
# 낙타체: 각 어절의 첫 글자를 대문자로 (TotalNumberofTables) - C 계열. Java에서는 자제
# 뱀체: 언더바 활용
# > 뜻이 통하게, 변수명 자체가 긴 것은 문제 없음
# > 한글 자제; 대문자 시작은 가능한 한 피할 것

# 예제 1: 식당의 테이블 수 = 10 (정수)
rest_table_num = 10
print(rest_table_num)

# 예제 2: 별점 4.3 (실수)
rest_rating = 4.3
print(rest_rating)

# 예제 3: 식당 이름 = 김밥천국종로점 (문자열)
rest_name = '김밥천국종로점'
print(rest_name)

# 예제 4: 식당 영업 여부 (논리형)
rest_is_open = True
print(rest_is_open)

# 예제 5: 내 스마트폰의 모델명
self_phone_model = 'iPhone 13 mini'
print(type(self_phone_model))
# 예제 6: 내 전화번호
self_phone_num = '01012345678'
print(type(self_phone_num))
# 예제 7: 내 스마트폰의 가격
self_phone_price = 950000
print(type(self_phone_price))
# 예제 8: 내 스마트폰의 화면 규격
self_phone_screensize = 5.4
print(type(self_phone_screensize))

print('모델명 '+self_phone_model)
print('전화번호 '+self_phone_num)
print('가격 '+self_phone_price)
print('화면 규격 '+self_phone_screensize)

# 자료형 (Data Type)
#   > 정수: int
#       > byte, short, int, long 종류에 따라 달라지는 할당 용량
#   > 실수: float
#   > 논리: bool
#   > 문자열: str
#       > '연산에 의미가 있는 것'이 숫자. 전화번호, 주민번호는 str