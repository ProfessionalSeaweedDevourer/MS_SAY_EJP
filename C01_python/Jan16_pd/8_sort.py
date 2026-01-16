# 와라 또이타닉 
import pandas as pd
df = pd.read_csv("titanic.csv")

# 이름을 기본 인덱스로 설정
df = df.set_index(df["Name"])
print(df)
print("-----")

# 인덱스 이외의 필드로도 여전히 정렬이 가능하다.
df = df.sort_values(by="Age")
print(df)