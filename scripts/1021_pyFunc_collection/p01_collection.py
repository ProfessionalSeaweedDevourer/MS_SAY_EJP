# collection : 데이터들을 표현할때 사용
# list : 주력 -> NumPy(list 기능개선판)
a = [1, 1, 1, 20, 50, 12, 4, 1]
print(a)
print(a[3])

# set : 중복x, 순서? -> 주력으로 쓰기는...
# 1) 어디서 데이터 받아와서 list로
# 2) 근데 중복을 없애야 한다면
a = set(a)  # list -> set
a = list(a)  # set -> list
print(a)

# dict : 순서x, 키-값 -> 활용도 높음
student = {"홍길동": {"국어": 50, "영어": 30},
           "김길동": 80}
print(student["김길동"])
# 다차원list : 유지보수의 시대에 알아보기 힘들
# dict + list조합으로 표현
print(student["홍길동"]["국어"])

print(list(student.keys())) # 키만 추출

print("최길동" in student) # 학생중에 최길동이 있나