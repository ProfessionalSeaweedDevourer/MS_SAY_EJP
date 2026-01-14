# 인공신경망이 다룰 데이터: 데이터의 짜임새, 구조는 인간이 설계.

import numpy as np

a = np.zeros([3, 2], dtype = np.int64) # 생성과 더불어 자료형 설정도 가능
print(a)

b = np.ones([4, 2])
print(b)

c = np.empty([2, 3]) # 어차피 바뀔 값이므로 아무거나 넣어서 만들기
print(c) 

d = np.arange(3, 10, 2) # python의 range와 유사: 3 - 10을 2 간격으로 => 3, 5, 7, 9
print(d)

e = np.random.rand(3, 2) # 0 - 1 사이의 임의의 값
print(e)

f = np.random.randn(3, 2) # 평균 0, 표준편차 1 => 정규분포 생성. 입력값은 결과의 크기 설정 (3*2)
print(f)

g = np.random.randint(1, 5, [3, 2]) # 1 - (5-1) 을 3*2로
print(g)