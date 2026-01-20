import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한국어 글꼴 설정
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size = 10).get_name()
plt.rc("font", family=fontName)

xData = np.array([10, 20, 30, 40, 50])
yData = [22, 56, 2, 10, 3]

# 제목
plt.plot(xData, yData)
plt.title("테스트 제목 1") # 기본값의 위치 (loc)는 middle임을 확인 가능.
plt.title("테스트 제목 2", loc = "left")

# 폰트
d = {"fontsize": 20, "fontweight": 900, "color": "#EC458B"}
plt.title("테스트 제목 3", loc = "right", fontdict = d)

plt.show()


