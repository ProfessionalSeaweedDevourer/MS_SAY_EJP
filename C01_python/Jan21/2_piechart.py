import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한국어 글꼴 설정
fontFile = "C:/Windows/Fonts/malgun.ttf"  # 한국어에 대응하는 맑은고딕 로드
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False  # 한글 폰트 적용 시 "-" 가 깨지는 문제 방지
# 여기까지가 템플런임 (맷 하하하)

# 파이 차트는 대표적으로 '점유율'의 시각화에 활용된다.
data = [28, 1, 10]
label = ["901", "903", "902"]

e = [0, 0, 0.3]
w = {"width": 0.7, "edgecolor": "black", "linewidth": 3} 

# plt.pie()의 매개변수 활용
plt.pie(data, labels=label, autopct="%.1f%%", startangle=45, explode=e, wedgeprops=w)
# 1) data: data를 파이 차트로 만든다.
# 2) labels: label 리스트를 사용해 레이블링한다.
# 3) autopct: 각 '조각'이 차지하는 비율을 자동 계산하여 첫째 자리까지 %로 띄운다.
# 4) startangle: '그리기 시작점'을 45도로 지정한다.
# 5) explode: 모든 조각을 리스트 'e'의 값에 따라 떨어뜨려 놓는다. 즉, 여기에서는 3번째 조각만 0.3만큼 띄운다.
# 6) wedgeprops: 파이와 각 조각의 '테두리'를 딕셔너리 형태의 데이터를 받아 그에 맞는 형식으로 꾸민다.

# plt는 주어진 data 그 자체는 건드리지 않는다 => '큰 것부터 정렬' 등은 따로 수동으로 하고 나중에 띄워야 한다.
plt.show()
