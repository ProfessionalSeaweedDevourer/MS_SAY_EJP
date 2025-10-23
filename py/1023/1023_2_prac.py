# 실습 2: 입력값 검증
# '정상적인 입력이 들어올 때까지 도로 보내기'가 재귀함수의 실전 활용처.

# 입력과 검증 함수
def isInputEven():
    n = int(input("임의의 짝수를 입력하세요: "))
    print("---------")

    if n%2==0:
        print(f"입력한 숫자는 {n}")
    else:
        print("입력된 수는 짝수가 아닙니다.")
        return isInputEven()

# 실행
isInputEven()


