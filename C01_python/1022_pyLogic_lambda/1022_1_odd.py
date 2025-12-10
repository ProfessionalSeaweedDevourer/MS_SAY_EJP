# 실습: 정수의 홀수 여부 판별 함수 만들기

def printisodd(n):
    if n%2==0:
        print("입력한 수는 짝수입니다.")
    else:
        print("입력한 수는 홀수입니다.")

n = int(input("임의의 정수를 입력하세요. \n"))
printisodd(n)

# 더 짧은 답안
def getisodd(n):
    return n % 2 != 0 # '구하기'와 '출력하기'는 다르다. return은 '반환'한다.

print(getisodd(n))
