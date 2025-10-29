# 실습: 사칙연산

# x, y를 순서대로 입력받음
# 입력받은 값에 대해 +, -, *, / 를 순차 수행하고 결과 출력

class Calculate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 입력 검증 - y가 0이면 나눗셈이 성립하지 않음. 나눗셈 소숫점 자릿수도 문제
# try - catch의 활용.

    def run(self):
        return(x+y, x-y, x*y, x/y)
    


if __name__ == "__main__":
    x =int(input("x: "))
    y = int(input("y: "))

    try:
        d = x / y
        print(d)

    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")

# 리스트에 있어야 할 게 없으면 뜨는 IndexError 등.
# 정확하게 케이스를 정하지 않고 except: 로 해도 처리는 가능; 

calcxy = Calculate(x,y)
print(calcxy.run())

