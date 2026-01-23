# =======================================================
# [0] plt 그 긴 거
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한국어 글꼴 설정
fontFile = "C:/Windows/Fonts/malgun.ttf"  # 한국어에 대응하는 맑은고딕 로드
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False  # 한글 폰트 적용 시 "-" 가 깨지는 문제 방지
# 여기까지가 템플런임 (맷 하하하)
# =======================================================

# =======================================================
# [1] 데이터 로드: 또이타닉
import pandas as pd

df = pd.read_csv("titanic.csv")
# =======================================================

# =======================================================
# [2] 실습 1: 등급(Pclass)에 따른 사망자 수 파이 차트

import matplotlib.pyplot as plt

# 1. 데이터 가공 (사망자 수 산출)
# Survived 값에 따른 '사망자 수' 산출
df["사망자 수"] = df["Survived"].apply(lambda x: 1 if x == 0 else 0)
# '사망자 수'를 'Pclass'에 따라 분리한 pclass_death_counts 생성, 합산
pclass_death_counts = df.groupby("Pclass")["사망자 수"].sum()
total_deaths = pclass_death_counts.sum()

# 2. 파이 차트 생성에 필요한 변수 정의
data = pclass_death_counts.values  # 각 등급별 사망자 수 수치
labels = [f"Class {i}" for i in pclass_death_counts.index]  # 등급 이름을 레이블로 변환

# 사망자 수가 가장 많은 등급을 찾아 해당 조각만 0.1만큼 돌출
explode_1 = [0.1 if count == pclass_death_counts.max() else 0 for count in pclass_death_counts]

wprops = {"width": 0.7, "edgecolor": "black", "linewidth": 2}

# 3. 파이 차트 그리기
plt.pie(
    data, 
    labels=labels, 
    # 비율(pct)을 사용하여 실제 명수와 백분율을 동시에 표시
    autopct=lambda pct: f'{int(round(pct * total_deaths / 100))}명\n({pct:.1f}%)', 
    startangle=90, 
    explode=explode_1, 
    wedgeprops=wprops
)

plt.title("좌석 등급별 사망자 수")
plt.savefig("pclass_death_counts.png", dpi=300, bbox_inches='tight')
# show()로 메모리 할당 해제되기 전에 별도 파일로 저장

plt.savefig("pclass_death_counts_transparent.png", dpi=300, bbox_inches='tight', transparent=True) # 투명 배경
plt.show()

# =======================================================

# =======================================================
# [2-1] 실습 1.1: 등급(Pclass)에 따른 '사망률' 파이 차트

# pclass_death_counts와 전체 인원수를 활용해 사망률 계산
pclass_total_counts = df.groupby("Pclass")["Survived"].count()
pclass_death_rates = pclass_death_counts / pclass_total_counts

data = pclass_death_rates.values
labels = [f"Class {i}" for i in pclass_death_rates.index]

# 가장 높은 사망률을 가진 등급 강조 (idxmax 활용)
explode_2 = [0.1 if i == pclass_death_rates.idxmax() else 0 for i in pclass_death_rates.index]

# autopct 내부에서 순차 접근을 위한 리스트 준비
m_list = pclass_death_counts.tolist()
n_list = pclass_total_counts.tolist()

# 시각화
plt.pie(data, labels=labels, 
        # m명 / n명 꼴의 텍스트와 비율을 함께 띄움
        autopct=lambda pct: f"{m_list.pop(0)} / {n_list.pop(0)}\n({pct:.1f}%)", 
        startangle=90, 
        explode=explode_2, wedgeprops=wprops)
plt.title("좌석 등급별 사망률")
plt.savefig("pclass_death_rates.png", dpi=300, bbox_inches='tight')

plt.savefig("pclass_death_rates_transparent.png", dpi=300, bbox_inches='tight', transparent=True) # 투명 배경
plt.show()
# =======================================================