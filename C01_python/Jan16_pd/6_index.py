import pandas as pd

a = pd.read_csv("titanic.csv")
print(a)
print("-----")

print(a.shape)

print(a.columns)

# 행 기준의 특정 데이터 조회
print(a.iloc[1])
print("-----")
print(a.iloc[1:5]) # 1부터 5 전까지 (=4) 의 데이터 조회
print("-----")

# >> index는 primary key와 유사하게 '기준'이 된다. 기본은 0,1,2,3... 꼴.
a = a.set_index(a["Name"])
print(a)
print("-----")
print(a.loc["Behr, Mr. Karl Howell"])
print("-----")
print(a.loc["Montvila, Rev. Juozas" : "Behr, Mr. Karl Howell"]) # loc도 이런 식으로 범위 조회가 가능하다.

# 행과 열을 지정하여 찾기
print(a.loc["Behr, Mr. Karl Howell"]["Age"])
print(a.loc["Behr, Mr. Karl Howell"][["Pclass", "Age"]])

# 를 그냥 , 로 쓰기
print(a.loc["Behr, Mr. Karl Howell", "Age"])
print(a.loc["Behr, Mr. Karl Howell", ["Pclass", "Age"]])

# 확장: 조건에 따라...

print(a[a["Age"] > 30]["Age"])

# 실습: 20대 인물의 이름, 나이, 등급
result = a.loc[(a["Age"] >= 20) & (a["Age"] < 30), ["Name", "Age", "Pclass"]]
print(result)