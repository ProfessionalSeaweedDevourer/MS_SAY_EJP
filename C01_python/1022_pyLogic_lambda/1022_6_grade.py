# 중간고사와 기말고사 성적을 입력받아 평균을 구하는 함수.

MidTerm = int(input("중간고사 : "))
Final = int(input("기말고사 : "))
avg = (MidTerm + Final) / 2
print("----------------")
print(f"평균점수 : {avg} 점")

# if avg >= 80:
#     print("고득점을 축하합니다.")
# else:
#     print("개허접")
#     if avg >= 70:
#         print("공부하세요.")

if avg >=90:
    print("A")
elif avg >=80:
    print("B")
elif avg >=70:
    print("C")
elif avg >=60:
    print("D")
else:
    print("E")