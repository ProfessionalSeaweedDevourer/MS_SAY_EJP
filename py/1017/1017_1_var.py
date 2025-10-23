# 예제 1: '다이제 미니' 과자 이름의 자료형과 출력
from ctypes import addressof


snack_name = "다이제미니"
print(snack_name)
print(type(snack_name))
print("----------------")

# 예제 2: 과자 가격 '5000'의 자료형과 출력
snack_price = 5000
print(snack_price)
print(type(snack_price))
print("----------------")

# 저장공간의 관리
# Static / Stack / Heap
#   > Stack: 아래부터 차곡차곡 쌓기
#       >> int와 같이 (상대적으로) 작은 정보는 stack으로
#   > Heap: OS 임의로 관리되는 공간
#       >> 문자열과 같이 (상대적으로) 큰 정보는 heap으로
#           >>> 그러나, '변수'는 항상 stack에 있음 - heap 상의 값과 연결
#   > python은 변수는 stack, 데이터는 heap에 저장하는 것이 기본

# 예제 3: 이름 '보드마카', 가격 500 - 자료형과 주소값의 확인 후 출력

item_name = "보드마카"
item_price = 500

print("제품명:", item_name)
print(id(item_name))
print(type(item_name))
print("---------------")

print("가격:", item_price)
print(id(item_price))
print(type(item_price))

print("제품명:", item_name, "/ " "가격:", item_price)

# 형식 지정 출력: String, Decimal, Float, Boolean
print("제품명: %s" % item_name)
print("가격: \\ %d" % item_price)

item_isBlack = True
# print("흑색 여부: %b" % item_isBlack)
# %b는 python에 존재하지 않음

item_size = 12.93212958
# 강제 자릿수 설정
print("규격: %.3f cm" % item_size)
print("가격: \\ %06d" % item_price)

hum=40.3435
print("습도: %0.1f%%" %hum)

# 여러 변수를 한 번에 출력
print("제품명: %s, 가격: \\ %d" % (item_name, item_price))
