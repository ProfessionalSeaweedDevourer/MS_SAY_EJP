import pandas as pd

df = pd.read_csv("seoul_air_quality_data.csv")

print(df.head())

# === 실습 ===

# 1) 측정소명 기준 PM과 FPM의 평균
print(df.groupby("측정소명")[["PM", "FPM"]].mean())
# df.groupby 메소드는 기본적으로 ()으로 호출.
# 여러 칼럼을 리스트 꼴로 대상으로 삼기 위해 []로 둘러쌈.
# 선택 대상 리스트 바로 밖에 .mean() 적용.

# 2) 권역별 PM과 FPM의 평균
print(df.groupby("권역명")[["PM", "FPM"]].mean())
print("-----")

# 3) 권역명과 측정소명 기준, PM과 FPM의 합계에 대한 평균
df["미세 및 초미세"] = df["PM"] + df["FPM"]
print(df.groupby(["권역명", "측정소명"])["미세 및 초미세"].mean())