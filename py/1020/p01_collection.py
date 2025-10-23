# 변수 : int/float/str/bool
#   데이터 담는 그릇
#   변수1 : 데이터1

# 컬렉션
#   변수중에 데이터 여러개 담을 수 있는거
#   변수1 : 데이터n
#   기본 컬렉션
#       List계열 - Python의 list
#       Set계열  - Python의 set
#       Map계열  - Python의 dict
#   Python은 BigData/AI에 특화된 언어
#       -> 기본 컬렉션 이외에 다양한 컬렉션이

s = "그냥 글자를 하나 써봅시다"
print(s, type(s))
# str에서 특정글자에 접근할때 list처럼
print(s[1])
print(s[1:5])
print("-----")

# 학생1명의 국어점수 80
kor = 80
print(kor, type(kor), id(kor))
print("-----")

# list : 평범
# 학생5명의 국어점수?
kor = [90, 50, 30, 11, 60, 100, 35, 43, 65, 78, 99, 0, 54]
print(kor)
print(type(kor))
print(id(kor))
print(len(kor))  # 몇개들어있냐
print(kor[1])  # kor에서 1번데이터(0부터 셈)
print(kor.index(50))  # 50은 몇번데이터일까
print(kor[2:5])  # kor에서 2 ~ (5-1)번 데이터
print(kor[3:10:2])  # kor에서 3 ~ (10-1)번 데이터, 2칸씩
print(kor[:10:2])
print(kor[3::2])
print(kor[3:10:])
print(kor[::2])  # 안쓰면 알아서
print(kor[::-1])  # 역순

kor.append(88)  # 뒤에 88추가
kor.insert(2, 77)  # 2번자리에 77추가(한칸씩 밀고)
kor[0] = 100  # 0번데이터 100으로 수정
del kor[1]  # 1번데이터 삭제

print(kor)
print("-----")

# set : 중복x, 순서? -> 활용하기가...
eng = {12, 54, 76, 12, 54, 100, 33, 76}
print(type(eng))
print(len(eng))
print(eng)
print("-----")

# dict : 순서x, 키-값 형태
mat = {"홍길동": 100, "김길동": 50, "최길동": 30}
print(type(mat))
print(mat["김길동"])