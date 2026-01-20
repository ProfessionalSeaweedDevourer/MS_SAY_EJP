import pandas as pd
 
df = pd.read_csv("lnps.csv", names=["마트","품명","가격","날짜","종류","구",])
print(df)
print("-----")
print(df["품명"].isnull()) # 값이 없나 확인
print("-----")
print(df[df["품명"].isnull()])
print("-----")
df["품명"] = df["품명"].fillna("몰라") # 없는거 채우기
print(df[df["품명"].isnull()])
print("-----")
 
# 없애기
# pandas로 '없다'가 표현불가
import numpy as np
 
df["품명"] = df["품명"].replace("몰라", np.nan)
print(df[df["품명"].isnull()])
# 0, "" : 값은 있는데 0/""일뿐 -> 계산/메소드 사용가능
# null/None/... : 값 자체가 없는 -> 불가능