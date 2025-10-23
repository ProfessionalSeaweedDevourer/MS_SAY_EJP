# 1, 2, 4, 8
# 1-15 사이의 입력값 value를 받아서, 1, 2, 4, 8 각각에 해당하는 특징이 있는지를 출력
# 가능한 조합을 모두 생각해 보자.
# 1, 2, 3(1+2), 4, 5(1+4), 6(2+4), 7(1+2+4)... 2진법이니까 당연히 죄다 가능함
# '자릿수'를 넘어가면, 그 자릿수에서 가능한 최대 수는 무조건 들어감
# 그러면 역으로 8부터 4, 2, 1로 내려가야 함
# while을 써야?

# 나의 답안
value = int(input("매장 특성: "))

while value>=8:
    print("주차장 보유")
    value-=8
    break
while value>=4:
    print("흡연실 보유")
    value-=4
    break
while value>=2:
    print("24시간 운영")
    value-=2
    break
while value>=1:
    print("Wi-Fi 제공")
    break

# for문으로 압축하기
# # 모범 답안
# value = int(input("매장 특성: "))

# # 특성 이름 리스트 (인덱스 0이 2^0, 인덱스 3이 2^3에 해당)
# features = ["Wi-Fi 제공", "24시간 운영", "흡연실 보유", "주차장 보유"]

# # 가장 낮은 비트(2^0)부터 가장 높은 비트(2^3)까지 확인
# for i in range(len(features)):
#     # i번째 비트에 해당하는 마스크 생성 (1 << i) = 2^i
#     mask = 1 << i
    
#     # value와 mask를 비트 AND 연산하여 해당 비트가 설정되었는지 확인
#     if value & mask:
#         # 해당 비트에 매칭되는 특성 출력
#         print(features[i])