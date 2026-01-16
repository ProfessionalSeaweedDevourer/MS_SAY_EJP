import pandas as pd

nps = pd.read_csv("seoul_nps_2024.csv", encoding="cp949") # 한국어 인코딩 적용하여 해결.
print(nps.head())

# 예시: 강남구 기준 배추 1포기 데이터
cab_gangnam = nps[(nps["자치구 이름"] == "강남구") & (nps["품목 이름"].str.contains("배추"))]
print(cab_gangnam[["시장/마트 이름", "품목 이름", "가격(원)"]].head())