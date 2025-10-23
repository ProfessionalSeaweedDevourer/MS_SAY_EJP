# 실습 1: 임의의 '위치'의 피보나치 수열 값 구하기 (1,1,2,3,5,8,13...)
# 1, 1 (여기까지 고정) 2(f(1)+f(2)) 3(f(2)+f(3))

def getfib(n):
    if n <= 1:
        return n
    else:
        return getfib(n-1) + getfib(n-2)

n = int(input("1 이상의 자연수 하나를 입력하십시오.\n"))
print(getfib(n))
