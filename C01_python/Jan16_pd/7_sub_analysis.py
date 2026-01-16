print(df[df["역"].str.contains("입구")])
# 그 외에도 startswith, endswith 등 메소드로 '~가 들어가는', '~로 시작하는', '~로 끝나는'의 검색이 가능.
# >> 예시: 역명이 서울로 시작하는 데이터에서의 역명, 하차 수, 승차 수
print(df[df["역"].str.startswith("서울")]["역", "승차", "하차"])