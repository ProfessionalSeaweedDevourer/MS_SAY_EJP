import pandas as pd

a = pd.DataFrame()
a["상품명"] = ["후렌치파이", "초코송이"]
a["가격"] = [3780, 2957]
print(a)
print("-----")

# Pandas 1.x 시절 => append로 pd.Series, dict 등 추가 가능
# (현행) Pandas 2.x => append 혼란을 막기 위해 삭제, df '붙이기'만 가능
s = pd.Series(["도리토스", 3350], index=["상품명", "가격"])
# 이에 대한 a = a.append(s) 는 이제 불가능.

# 그러므로, 여기에서는 s를 또 하나의 df로 바꾸고 그 결과물을 a와 합칠 필요가 있음.
s = pd.DataFrame([s]) # pd.Series인 s를 df로 변환
print(s)

# 붙이기: concat
a = pd.concat([a, s])
print(a)