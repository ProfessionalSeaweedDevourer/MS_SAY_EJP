import pandas as pd
 
df = pd.read_csv("lnps.csv", names=["마트","품명","가격","날짜","종류","구",])
df = df.set_index(df["마트"]) # 마트이름으로 찾을수있게
df = df.sort_index() # 마트이름 가나다순 정렬
print(df) # 전체출력
print("-----")
 
print(df.loc["통인시장"]) # 통인시장 데이터만
print("-----")
 
df["마트"] = df["마트"].fillna("모름")
print(df[df["마트"].str.contains("가락")]) # 마트명에 '가락' 들어있는 데이터만
print("-----")
 
df["품명"] = df["품명"].fillna("모름")
print(df[df["품명"].str.contains("사과")][["마트", "품명"]]) # 사과는 어떤 마트에서 살 수 있나
print("-----")
 
df = df.sort_values(by=["품명", "가격"], ascending=[True, False]) # 품명 가나다 -> 가격 비싼순 정렬
print(df) # 전체출력
print("-----")
 
print(df[df["가격"] >= 30000] [["품명", "가격"]]) # 30000원 이상인 데이터 품명, 가격
print("-----")
 
# 종로구 데이터만 반복문으로 하나하나 출력
jongroDF = df[df["구"] == "종로구"]
for i, v in enumerate(jongroDF.index):
    print(jongroDF.iloc[i])
    print("---")