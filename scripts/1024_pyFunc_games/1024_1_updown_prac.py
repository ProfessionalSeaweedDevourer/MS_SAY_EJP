# 1) 1 - 10,000 사이 무작위 정수 하나를 미리 선출
# 2) 정수를 입력받음: 이것보다 크면 UP, 작으면 DOWN 출력하고 반복
# 3) 맞추면 몇 번 만에 맞췄는지 출력하고 종료

from random import randint

answer = randint(1,10000)
guess_count = 0

print(f"{answer}") #디버그용

while True:
    guess = input("1 - 10,000 사이 정수 하나를 입력하십시오: ")
    guess_count+=1

    if int(guess) < answer:
        print("UP")
    elif answer < int(guess):
        print("DOWN")
    else:
        print(f"{guess_count}회만에 정답!")
        break
    print("--------")


# # 개선된 코드 (단축 버전):
# while (guess := int(input(f"1 - 10000 사이 정수 입력: "))) != answer:
#     guess_count += 1
#     print("UP" if guess < answer else "DOWN") # print 내에 if 판정이 가능하다.
#     print("--------")
    
# # 정답 처리 및 종료 (루프 탈출 후):
# guess_count += 1
# print(f"{guess_count}회 만에 정답!")