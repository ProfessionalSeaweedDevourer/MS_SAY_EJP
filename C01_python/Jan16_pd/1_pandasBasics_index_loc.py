# np.array: 기능이 추가된 List
# Pandas: 파이썬 데이터 분석 전용 라이브러리
# pd.dataframe: 코드로 다루는 액셀 같은 것
import pandas as pd

# list 같은 무언가
a = pd.Series([1, 234, 534, 980])
print(a)
print("-----")
print(a[1])
print("-----")

# Excel 맛의 무언가
b = pd.DataFrame()
b["이름"] = ["새우깡", "양파링"] # KVS 형식으로 데이터 프레임을 형성
b["가격"] = [3000, 4000]
print(b)
print("-----")
print(b["이름"]) # 특정 필드만 조회 - DB처럼 다루기

# index 활용: 검색 기능

# "이름" 열을 인덱스로 설정
b = b.set_index("이름")

print(b)
print("-----")

# loc: 인덱스 이름(Label)으로 찾기
print(b.loc["새우깡"]) 

print("-----")

# iloc: 정수 위치(Position)로 찾기 (0부터 시작)
print(b.iloc[1])