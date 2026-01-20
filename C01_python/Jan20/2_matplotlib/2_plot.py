import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한국어 글꼴 설정
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 10).get_name()
plt.rc("font", family=fontName)
# 여기까지가 템플런임 (맷 하하하)

# 꺾은선그래프
import pandas as pd

df = pd.read_csv("seoul_air_quality_data.csv")

# "측정소명"이 "종로구"인 데이터의 "PM"과 "FPM"을 그린 꺾은선 그래프 출력하기.
# 가로축이 "측정일시"
data = df[df["측정소명"] == "종로구"]
plt.plot(data["PM"], label = "PM")
plt.plot(data["FPM"], label = "FPM")
plt.title("종로구 미세먼지와 초미세먼지 농도 변화")
plt.xlabel("측정일시")
plt.ylabel("농도")

plt.show()