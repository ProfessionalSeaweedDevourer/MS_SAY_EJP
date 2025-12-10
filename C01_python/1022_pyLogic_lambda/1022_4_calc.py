# 실습 4: 사칙연산의 실행과 반환


def calc(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return (a,b,c,d) # 괄호를 안 넣어도 작동하지만 보기에 헷갈릴 수 있다. return은 언제나 한 번만 가능하며, 전체를 tuple로 반환한 것.


a, b = map(int, input("두 정수를 띄어쓰기로 구분하여 입력하세요: ").split())

# print(calc(a, b))

x, y, z, _ = calc(10,5) #tuple로 나눠 받기. 안 받고 싶은 것은 _로 처리.
print(x,y,z)