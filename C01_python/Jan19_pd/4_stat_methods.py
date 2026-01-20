import pandas as pd
 
df = pd.read_csv("lnps.csv", names=["마트","품명","가격","날짜","종류","구",])
 
print(df["가격"].max())
print("-----")
print(df[df["가격"] == df["가격"].max()])
print("-----")
print(df["가격"].min())
print(df[df["가격"] == df["가격"].min()])
print("-----")
print(df["가격"].mean()) # 평균값
print(df["가격"].median()) # 중앙값
print(df["가격"].mode()) # 최빈값(가장 많이 나오는) -> Series로 나옴
print(df["가격"].sum())
print(df["가격"].count())
print(df["가격"].var())
print(df["가격"].std())
print(df["가격"].describe()) # 모든 주요 통계량 항목을 한꺼번에, 제목도 붙여서 보여주기.