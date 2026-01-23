import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한국어 글꼴 설정
fontFile = "C:/Windows/Fonts/malgun.ttf"  # 한국어에 대응하는 맑은고딕 로드
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False  # 한글 폰트 적용 시 "-" 가 깨지는 문제 방지
# 여기까지가 템플런임 (맷 하하하)

import pandas as pd

df = pd.read_csv("subway.csv")