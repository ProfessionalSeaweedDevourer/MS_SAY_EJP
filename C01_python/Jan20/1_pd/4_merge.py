import pandas as pd

df1 = pd.read_csv("titanic.csv")
df2 = pd.read_csv("titanic.csv")


df3 = pd.concat([df1, df2]) # concat: 단순히 '이어붙이기'
print(df3)
print("-----")

df4 = pd.concat([df1, df2], axis = 1)
# axis = 1(열)로 지정하고 '붙이기': '수직'이 아니라 '수평'으로 붙음 => JOIN
print(df4)
print("-----")

# =============================================================
snack = pd.DataFrame()
snack["제품명"] = ["새우깡", "빼빼로"]
snack["판매가"] = [3000, 2000]
snack["제조사"] = ["농심", "롯데"]

company = pd.DataFrame()
company["제조사"] = ["농심", "롯데"]
company["위치"] = ["서울", "제주"]

# 이렇게 겹치는 이름의 칼럼이 있을 때, 'merge'를 통한 JOIN이 가능하다.
df_combined = pd.merge(snack, company)
# merge는 별도의 입력이 없어도, 공통의 칼럼인 '제조사'를 기준으로 두 df를 엮는다.
print(df_combined)

# 공통으로 존재하는 칼럼이 여러 개일 경우에는 기준 칼럼을 수동 지정해야 한다.
df_combined_selected = pd.merge(snack, company, on = "제조사")

# 내용물은 같지만 칼럼명이 다른 칼럼이 서로 존재하는 경우에는...
# 예를 들어 company에서는 "제조사"가 "사명"일 경우에는,
df_on = pd.merge(snack, company, left_on="제조사", right_on="사명")