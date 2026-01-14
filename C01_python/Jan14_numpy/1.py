# 일반적인 list
score = [[100, 90, 30], [50, 30, 80]]

print(score)
print(type(score))
print(score[0])
print(score[0][1])
print("-----")

# -----------------------------
# 데이터 조작
# -----------------------------

score[1][2] = 0 # 2번 학생의 2번 과목 성적을 0으로 설정
# score[1][0:2]=0
# 2번 학생의 모든 과목(0~2번) 성적을 0으로 설정...?
# list는 한 번에 여러 개의 데이터를 수정할 수 없음.

# np.array 활용
import numpy as np

score2 = np.array(score)

print(score2)
print(type(score2))
print(score2[0])
print(score2[0][1]) # 기존 list식 다루기
print(score2[0, 1]) # numpy에서만 가능한 방식: 고차원에서 접근이 편리함
print("-----")

# -----------------------------
# 데이터 조작
# -----------------------------
score2[1][0:2] = 0 # np.array는 동시에 여러 개의 값을 수정 가능. => Slicing
print(score2[1])

print(score2.shape) # 데이터의 '형태' 보기 => 2행 3열