import pandas as pd

df = pd.read_csv("mosquito.csv", names=["측정시기", "물가", "가정", "공원"])
print(df)

# # 물가, 가정, 공원 각각 평균값 내서 어디가 모기 가장 심한지 보이기
# print((df["물가"] + df["가정"] + df["공원"]) / 3)
