from time import sleep

# 실습 2: 임의의 정수를 2배 하는 함수

from time import sleep


def doubling(n):
    return n*2

n=int(input("임의의 수를 입력하세요."))

# 또 다른 활용
sleep(doubling(n))

# 출력
print(doubling(n))

