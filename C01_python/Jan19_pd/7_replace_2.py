import pandas as pd

df = pd.read_csv("titanic.csv")
df = df[["Name", "Sex"]] # 이름과 성별만을 뽑아오기

print(df)

# 성별을 한국어로 번역
df["Sex"] = df["Sex"].replace({"male": "남", "female": "여"})
print(df)

# 이름의 Mr. 부분만을 '미스터'로...? > 순수 Pandas에서 지원하는 기능은 아님.
# > df["Name"] = df["Name"].replace("Mr,", "미스터")
# >> 이것은 '이름 자체가 'Mr.'인 데이터에만 적용되므로 원하는 방식으로 작동하지 않음.
# 이에 대해서는 python으로 접근해야 함: "임의의 입력 문자열에서 Mr.를 '미스터'로 바꾸는 함수"를 만들자.
def mr_translate(name):
    return name.replace("Mr.", "미스터")

# apply 기능을 활용하여, replace_mr 함수를 df["Name"]의 모든 행에 일괄 적용
df["Name"] = df["Name"].apply(mr_translate)
print(df)

# 이름에서 성 부분을 빼고 본인 이름만 남기는 함수 만들기: 기준은 띄어쓰기
def familynameremover(name):
    return name.split(" ")[0]  # 띄어쓰기 기준으로 쪼갠 후, 첫 번째 부분(본인 이름)을 반환
df["Name"] = df["Name"].apply(familynameremover)
print(df)

# 이 정도의 짧은 일회용 함수라면, 람다 함수 꼴로 쓰는 것이 효율적.
df["Name"] = df["Name"].apply(lambda name: name.split(", ")[0])
print(df)