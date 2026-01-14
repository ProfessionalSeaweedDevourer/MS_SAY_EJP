a1 = [10, 20]
b1 = [5, 6]

c1 = a1 + b1
print(c1) # 실질적으로 아무 쓸모도 없는 '이어붙인' 것을 출력함

d1 = a1 * 3
print(d1) # 이 또한 '반복' 결과를 보여 줌 - '값'을 다루는 기능이 아님

print("-----")

import numpy as np

a2 = np.array([10, 20])
b2 = np.array([5, 6])

c2 = a2 + b2
print(c2) # 이쪽이 상식적이고 유용한 '더하기'의 기능. 형태가 같은 두 배열에 대해, 같은 자리의 원소를 더함.
# 가령 PM10과 PM25를 보고 '총 미세먼지'를 구하려고 할 때는 이 둘을 np.array꼴로 저장할 필요가 있음.

d2 = a2 * 3
print(d2) # 이쪽이 역시 더 쓸모 있는 기능.
# * Broadcasting: 형태가 다른 두 데이터를 연산할 경우, 결과물의 차원수는 더 높은 데이터의 차원으로 맞춰짐.

print("-----")

# 실습: 학생 3명의 성적 관리

name = np.array(["김정은", "마두로", "시진핑"])
kor = np.array([100, 90, 85])
eng = np.array([10, 50, 20])
math = np.array([40, 60, 55])

total = kor + eng + math
avg = total / 3

avg_int = avg.astype(int)

print(avg_int)

def passed(avg_score):
    if avg_score >= 60:
        return "합격"
    else:
        return "불합격"

for avg_score in avg_int:
     print(passed(avg_score))

print("-----")

# 또 다른 해결법: Masking

over60 = avg_int > 60
print(over60) # '조건' 달성 여부를 출력
print(name[over60]) # '조건' 달성한 원소만을 출력

# 마스킹 실습 1: 국어 만점
kor100 = kor == 100
print(name[kor100]) # 이런 것도 할 수 있다.

# 나아가서...
print(name[kor == 100]) # 이렇게 더 짧게 쓸 수도 있다. 서브쿼리 느낌

# 마스킹 실습 2: 영어 성적이 낮은 학생 (15점 - 60점)
print(name[(eng >= 15) & (eng <= 60)])

# 15 <= eng <= 60은 쓸 수 없다.
# 여러 개의 '조건'을 묶을 때 &을 사용한다.
# python의 and는 사실 && => 앞 조건이 틀리면 뒤 조건을 무시하게 된다.
# 나오다가 끊기면 의미가 없기 때문에 and는 쓸 수 없음.