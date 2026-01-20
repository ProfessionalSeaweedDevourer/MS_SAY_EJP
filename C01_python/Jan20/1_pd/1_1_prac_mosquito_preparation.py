import pandas as pd

# 1. 데이터 로드
df = pd.read_csv("mosquito.csv", names=["측정시기", "물가", "가정", "공원"])

# 2. 불필요한 필드 제거
df = df.drop(["물가", "공원"], axis=1)

# 3. 데이터 타입 변환 (가장 중요)
# 'noValue' 같은 문자열을 NaN(결측치)으로 강제 변환
df["가정"] = pd.to_numeric(df["가정"], errors='coerce')

# 4. 결측치 및 0인 데이터 제거
df = df.dropna(subset=["가정"]) # NaN 제거
df = df[df["가정"] > 0]        # 0보다 큰 값만 유지

# 5. (선택사항) 만약 100을 초과하는 값이 오류라고 판단된다면 100 이하만 필터링
# df = df[df["가정"] <= 100]

# 6. 평균 산출
print(df["가정"].mean())