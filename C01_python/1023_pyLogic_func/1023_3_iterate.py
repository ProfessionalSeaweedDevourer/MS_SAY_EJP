# # 실습 3: 반복문

# # 컬렉션 탐색

# a = [45, 234, 11, 100, 50]

# for i in a: # 이런 식으로 간편하게 i번 원소 출력 가능
#     print(i)

# print("----------------")

# for j in range(1,6):
#     print(j)

# print("----------------")

# # 예제: 0 - 4까지

# for k in range(0,5):
#     print(k)

# print("----------------")

# # 예제: 건너뛰기

# for i in range(2, 11, 2):
#     print(i)

# print("----------------")

# # 실습: 팩토리얼을 반복문으로 구현

# fac_to_10 = 1
# for i in range(1,11):
#     fac_to_10 *= i
    
# print(f"10! = {fac_to_10}")
# print("----------------")

# # 예제: 리스트에 차례대로 접근하기
# # 각 원소와 상호작용 가능: 조건에 따른 값 변경, 다음 원소와 비교, 여러 리스트의 병렬 처리 등(이름과 학번 출력하기)
# l = ["A", "B", "C", "D", "E"]
# for i in range(len(l)):
#     print(l[i])

# print("----------------")

# # 그냥 이렇게 호출해도 지금은 결과가 같음
# for j in l:
#     print(j)

# print("----------------")

# for i, v in enumerate(l): # 인덱스와 값을 i, v에 받기
#     print(i)
#     print(v)

# print("----------------")

# # 딕셔너리에서는 더욱 유용하다.
# d1 = {"Color": "Black", "Price": "500"}
# for k, v in d1.items():
#     print(k)
#     print(v)

# print("----------------")

# # 실습: 13579 출력
# for i in range(1,10,2):
#     print(i)

# print("----------------")

# # 실습: 97531 출력
# for i in range(9,0,-2):
#     print(i)

# print("----------------")

# # 실습: 1 - 10 더하기
# sum = 0
# for i in range(1,11):
#     sum+=i

# print(sum)
# print("----------------")

# # 실습: 1 - 19까지의 홀수만 더하기
# sum_odds = 0
# for i in range(1,20,2):
#     sum_odds+=i

# print(sum_odds)
# print("----------------")

# # 실습: 구구단 출력

# for i in range(2,10):
#     for j in range(1,10):
#         mult = i*j
#         print(f"{i} X {j} = {mult}")
# print("----------------")

# # 확장: 2*1, 3*1...9*1까지 나오고 2*2로 넘어가는 구조 만들기
# for j in range(1,10):
#     for i in range(2,10):
#         mult = i*j
#         print(f"{i} X {j} = {mult}")
# print("----------------")

# 실습: 역 피라미드
for i in range(5,0,-1):
    for j in range(i+1,1,-1):
        print("A", end="")
    print()

print("----------------")

# 실습: 계단
# A
#  A
#   A
#    A
#     A
for i in range(5):
    for j in range(i):
        print(" ", end="") # 공백을 반복하다가
    print("A") # <- 줄바꿈 없이 A 달고 줄바꿈

# 실습: 변화하는 홀수 피라미드
for i in range(6):
    for j in range(1,(i*2)):
        if i%2==1:
            print("A", end="")
        else:
            print("B", end="")
    print()

# 개선: 출력할 문자를 미리 결정하고 들어감 

for i in range(6):
    if i % 2 == 1:
        char_to_print = "A"
    else:
        char_to_print = "B"
        
    count = i * 2 - 1
    print(char_to_print * count)

# # 테스트: 3중
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             print("!", end = "")
#         print()
#     print()

# 실습: 1 - 20 가우스합
sum = 0
for i in range(21):
    sum+=i
print(sum)

print("------")

# 실습: 1 - 10 사이 무작위 정수 10회 출력

from random import randint
from re import L

for i in range(11):
    randNum = randint(1,10)
    print(randNum)

print("------")

# 실습: '4'가 나올 때까지 위를 반복

while randNum != 4:
    randNum = randint(1,10)
    print(randNum)

print("------")

# 실습: 임의의 정수를 입력받아 출력하되, 입력값이 5가 되면 종료.
# n = 0
# while n != 5 :
#     n = int(input("임의의 정수를 하나 입력하세요: "))
#     print(n)

# java의 do {} while (조건): 문: 초기 실행은 검사를 거치기 전에 수행됨.

# 실습: 1, 4, 7, 10, ... , 101까지 출력

# count = 1
# while count <= 101:
#     print(count)
#     count += 3

# # 반복문의 제어: break (종료)

# for i in range(1,100,3):
#     if i%10==0:
#         break
#     print(i)

# 실습

# textInput = "Sample"

# while textInput != "Stop":
#     textInput = input(("Chat: "))
#     print(textInput)

# # 초기화를 안 하고 해결하는 (일반적인) 방법: while True

# while True: # 일단은 계속 루프시킴
#     textInput = input("Chat: ")
    
#     if textInput == "Stop": # 돌리던 중에 검사 실시
#         break  # 사용자가 "Stop"을 입력하면 루프를 즉시 종료
        
#     print(textInput)

# # continue의 활용

# for i in range(1,100,3):
#     if i%10 == 0:
#         continue # 반복을 즉시 다시 수행 - 결과적으로, 10의 배수는 출력되지 않게 됨.
#     print(i)
# print("-----")

# 상위 반복문을 깨는 법

for i in range(3):
    for j in range(3):
        for k in range(3):
            if k == 1:
                break # 여기서 j나 i를 깨려면?
                # i = 3으로 강제 세팅해도 실패.
            print(i,j,k)