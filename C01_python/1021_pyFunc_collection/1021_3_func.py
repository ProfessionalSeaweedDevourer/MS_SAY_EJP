# 함수

## 1) 함수의 정의
def func_sample(): # 함수명 조건은 변수명 조건과 같음
     print("sampletext") # 들여쓰기는 필수
     print("----------")

# python은 기본적으로 뭘 따로 열고 닫지 않음. ":"과 들여쓰기를 활용

func_sample()
func_sample() # 실제로 호출하지 않으면 작동하지 않음

# 컴파일러 언어에는 반드시 main 영역이 존재 / 인터프리터 언어인 python에는 그런 게 없음
# 함수 자체를 '밖에서' 선언하는 타 언어와 다름

# 개발 중이라 아직 무슨 내용이 될지 잘 모르는 함수의 경우
def test():
    pass # placeholder
    print("나중에")

# 예시: 2개 수의 합 출력
def print_sum(a,b):
    c = a+b
    print(f"{a}+{b}={c}")
    print("-----------")

print_sum(10,20)
print_sum(20,20)

# 실습: 3개 수의 합 출력
def print_sumof3(a,b,c): # 변수는 각 함수에서 따로 정의되기 때문에 이름이 중복되어도 문제 없다.
    d = a+b+c
    print(f"{a}+{b}+{c}={d}")
    print("-------------")

print_sumof3(10,20,30)
print_sumof3(20,20,50)

# 예시 2: 2개의 글자 붙여 출력
def print_gluestr(a,b):
    pass

print_sum("ㅋ","ㅎ")

# python은 함수 인자의 기본값 지정이 가능하다.
def print_sumofstrs(o, p="ㅠ"):
    i = o+p
    print(i)

print_sumofstrs("ㅐ") # "ㅐㅠ"가 출력된다.

# # * Overloading: 파라미터 부분이 다르면 이름은 같지만 내용이 다른 함수를 여러 개 만드는 것이 허용된다.
# #     > 인수의 종류에 따라 자동으로 다른 기능을 할 수 있도록 한다.
# #         > python은 함수 인자에 기본값을 지정할 수 있기 때문에, overloading이 불가능하다.