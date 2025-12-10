from datetime import datetime # 패키지 datetime을 임포트
now = datetime.today() # datetime 모듈 내의 메서드 today 호출
print(now)
print(now.year)
print(now.month)
print(now.day)

d = datetime(2000,1,1)
print(d)

# 임의 날짜 받아서 하기
# d2 = input("yyyy/mm/dd : ")
# print d2 # 별로 편하지 않음

# 자체 지원 기능 쓰기
d3 = "2000/12/31"
# d3 = datetime.strptime(d3, "/")

#

d5 = datetime.today()
d5 = datetime.strftime(d5, "%Y.%m.%d %H:%S")
print(d5)

userbirthdate_input = input("생년월일(yyyy/mm/dd) : ") # 0000/00/00로 입력
# 이것을 / 기준으로 split하고 datetime 적용
userbirthdate = datetime.strptime(userbirthdate_input, "%Y/%m/%d")

#나이 계산
age = now.year - userbirthdate.year + 1
print(age)

#요일 계산
userbirthdate_daytime = datetime.weekday(userbirthdate)
weekdayList = ["월", "화", "수", "목", "금", "토", "일"]

print(f"{weekdayList[userbirthdate_daytime]}요일")