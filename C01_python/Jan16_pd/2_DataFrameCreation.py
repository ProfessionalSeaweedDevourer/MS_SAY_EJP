import pandas as pd

# 쌩 df
a = pd.DataFrame()
a["이름"] = ["김정은", "시진핑"]
a["체중"] = ["99", "158"]
print(a)
print("-----")

# np.array 꼴로 만든 df
b = pd.DataFrame()
b["이름"] = ["김정은", "시진핑"]
b["체중"] = ["99", "158"]
print(b)
print("-----")

# 2차원의 list / np.array로 만든 df
c = [["김정은", 99], ["시진핑", 158]]
c = pd.DataFrame(c, columns=["이름", "체중"])
print(c)
print("-----")

# dict가 있는 list로 만든 df...뭔가 낯선 형태로
d = {"이름": ["김정은", "시진핑"], "체중": [99,158]}
d = pd.DataFrame(d)
print(d)
print("-----")

# list + dict: JSON 형태로 만든 df
e = [{"이름": "김정은", "체중": 99}, {"이름": "시진핑", "체중": 158}]
e = pd.DataFrame(e)
print(e)

# pd.DataFrame() 함수는 => 일반 python 데이터를 Pandas에서 다룰 수 있는 꼴로 '변환'하는 장치.
