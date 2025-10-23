# model_name = input("기기 제품명을 입력하십시오: ")
# print("제품명: %s" % model_name)

# print(id(model_name), " / ", type(model_name))

# model_price = int(input("제품 가격을 입력하십시오: "))
# print("가격: \\ %d" % model_price)

# 입력을 '십만원'으로 하는 놈도 있을 것
#   > 출력에서는 %d가 아니라, 다른 유형의 입력값에도 대응할 수 있는 자료형을 써야 함
# 형변환(type casting): 자료형을 변환
#   > 자료형(변수명)

# 예제: 화면 크기 (인치, 실수) 입력 -> 소수점 2자리로 나오게 출력

model_size=float(input("기기 화면 규격을 인치로 입력하십시오: "))
print("화면 규격: %.2f 인치" % model_size)
