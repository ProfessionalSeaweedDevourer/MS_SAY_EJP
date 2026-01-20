import pandas as pd

df = pd.read_csv("titanic.csv")
df = df[["Name", "Age", "Survived"]]

# 함수를 만들어, '나이'를 10대 / 20대 / 30대 등으로 범주화하고 이를 apply.
def age_categorizer(age):
    if pd.isna(age):
        return "Unknown"
    elif age < 10:
        return "유아"
    elif age < 20:
        return "10대"
    elif age < 30:
        return "20대"
    elif age < 40:
        return "30대"
    elif age < 50:
        return "40대"
    elif age < 60:
        return "50대"
    elif age < 70:
        return "60대"
    elif age < 80:
        return "70대"
    else:
        return "80대 이상"
    
df["Age_Group"] = df["Age"].apply(age_categorizer)

# 나아가, 생존 여부의 0과 1을 각각 '사망', '생존'으로 대체. 이것은 람다 함수 꼴로도 가능할 것.
df["Survived"] = df["Survived"].apply(lambda status: "생존" if status == 1 else "사망")

print(df)