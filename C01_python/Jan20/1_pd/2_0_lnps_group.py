import pandas as pd

df = pd.read_csv("lnps.csv", names = ["매장", "품목", "가격", "날짜", "분류", "지역"])

print(df)   

print(df.groupby(["지역", "분류"])["가격"].mean()) # '지역'과 '분류'별 '가격의 평균'값을 산출