# 지금까지의 내용
#   함수와 소스 정리: 여러 번 활용을 쉽게
#   parameter: 함수 실행에 필요한 '재료'
#   return: 함수 결과의 '반환' 및 '완료'

# 람다 함수
name = lambda s: print(s)
s = str(input("이름을 입력하세요. "))
name(s)

# > lambda의 활용처: 그때그때 바로 값을 구해서 반환.
print((lambda a, b, c: (a + b + c) / 3)(10, 20, 55))

# 일반적인 함수로 선언할 경우
# def Avgof3(a,b,c):
#     return((a+b+c)/3)
