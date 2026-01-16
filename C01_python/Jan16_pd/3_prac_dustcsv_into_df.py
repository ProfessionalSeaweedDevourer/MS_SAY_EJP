import pandas as pd

a = pd.read_csv("seoul_air_quality_data.csv")

print(a.head()) # 인터렉티브 노트북 환경에서는 그냥 df.head()나 info()만 해도 나옴
print(a)

# '제목'이 안 붙은 csv를 df화하고 제목을 '붙여' 주는 것이 가능하다.
# b = pd.read_csv("titanic.csv", names=["년", "월", "일", "시","분"])
# print(b.head())

# 데이터의 종류에 따른 관리
# > 정형 데이터: OrcaleDB / .csv
# > 비정형 데이터: MongoDB / .txt

# 그런데 그냥 txt도 read_csv로 불러올 수 있다.
c = pd.read_csv("naverBlog.txt", on_bad_lines='skip')
print(c.head())

