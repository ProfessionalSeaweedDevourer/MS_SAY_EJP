import pandas as pd

df = pd.read_csv("titanic.csv")

# 로드 체크
print(df)
print("-----")

# 필드 단위의 삭제
df = df.drop("Survived", axis = 1) # Survived 필드를 삭제
# axis: 0이면 행, 1이면 열 => axis = 1로 지정함으로써, '이름이 Survived인 열을 지워라'로 명령 지정

df = df.drop(["Pclass", "Fare"], axis = 1) # []로 묶인 Pclass와 Fare 필드를 한 번에 삭제

# 실습: 더 많은 필드를 한 번에 삭제
df = df.drop(["Sex", "Parch", "Ticket", "Cabin", "Embarked"], axis = 1) # 나머지도 대충 다 지우기
# 그런데 이 많은 게 어차피 다 '필요 없어서' 그런 거라면...
# => 애초에 필요한 것만 '가져와서' 별도 df로 만들면 됨. 
# '삭제 작업'이라는 것이 애초에 필요한지는 상황에 따라 판단할 것.

print(df)

# 인덱스 기준의 데이터 삭제
df = df.drop(889)

# 인덱스 기준의 검색에 의한 삭제
df = df.set_index(df["Name"])
df = df.drop("Dooley, Mr. Patrick")
# 이름 인덱스의 둘리 패트릭을 삭제 (어떻게 사람 이름이)
