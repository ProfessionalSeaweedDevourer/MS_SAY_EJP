# list, set, dict의 개념과 활용
# 1. List (리스트): 순서가 있고, 중복을 허용하는 변경 가능한(mutable) 컬렉션 -> 데이터'들'

# # f-string과 {}를 이용한 변수 호출
name = "Charlie"
age = 25

# f-string 사용 예시
print(f"제 이름은 {name}이고, 나이는 {age}세입니다.")
# 출력: 제 이름은 Charlie이고, 나이는 25세입니다.

# 리스트 생성
my_list = [10, 20, 30, 20, "apple"]
print(f"1. 초기 List: {my_list}")

# 요소 접근 (인덱싱)
print(f"List의 첫 번째 요소: {my_list[0]}")

# 요소 추가
my_list.append(40)
print(f"요소 추가 후 List: {my_list}")

# ---------------------------------------------

# 2. Set (집합): 순서가 없고, 중복을 허용하지 않는 변경 가능한 컬렉션
# #     > set으로 변환하면 자동으로 중복 제거: 받아온 데이터를 list화 > set화 > 다시 list화 하여 다루기

# Set 생성 (중복된 20은 자동으로 하나만 남음)
my_set = {10, 20, 30, 20, "banana"}
print(f"2. 초기 Set: {my_set}")

# 요소 추가
my_set.add(50)
print(f"요소 추가 후 Set: {my_set}")

# 집합 연산 (Set은 주로 중복 제거, 교집합, 합집합 등에 사용)
another_set = {30, 40, 50, 60}
print(f"두 Set의 합집합: {my_set.union(another_set)}")

# ---------------------------------------------

# 3. Dict (딕셔너리): '키(Key)'와 '값(Value)' 쌍으로 이루어진 변경 가능한 컬렉션
# # list 내의 list를 만드는 것도 가능

# Dict 생성 (Key는 유일해야 함)
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "Seoul"
}
print(f"3. 초기 Dict: {my_dict}")

# 값 접근 (키를 이용)
print(f"Dict에서 'name'의 값: {my_dict['name']}")

# 새로운 키-값 쌍 추가 또는 기존 값 변경
my_dict["occupation"] = "Engineer"
my_dict["age"] = 31 # 값 변경
print(f"수정/추가 후 Dict: {my_dict}")

# ---------------------------------------------

# 활용 예시:
# List: 할 일 목록, 점수 기록, 순차적인 데이터
# Set: 고유 사용자 ID 목록, 중복 제거
# Dict: 사용자 프로필, 설정 정보, 데이터베이스 레코드

# 중첩된 딕셔너리
score = [[[[70,30], 50]]]
print (score[0][0][0])

# dict + list
student = {
    ["홍길동"]
        ["국어"]: 90 
}
print(student["홍길동"]["국어"])
print(list(student.keys())) # 키 부분만을 추출해서 리스트로 변환