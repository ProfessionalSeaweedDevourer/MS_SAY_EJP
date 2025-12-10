# Call by value, Call by reference
# Python은 Call by reference만 있음
d = 10
e = 10
################
def test(a, b, c):
    global e # 지금부터 이 공간에서 e라고 하면 4번줄의 그 e
    print("green", a, b[0], c[0])
    print(id(a), id(b), id(c))
    a = 100
    b[0] = 100
    c = [100, 200]
    d = 100 # green d 새로 만들고 100(3번줄의 d랑 상관없고)
    e = 100 
    print("green", a, b[0], c[0], d, e)
    print(id(a), id(b), id(c))
################
a = 10
b = [10, 20]
c = [10, 20]

# a따로, d따로, e따로 -> 각각 주소가 다 달라야
# 근데 셋다 값이 10
# Python이 다 같은 데이터인가 싶어서
#   -> 하나만 만들어서 같이 사용하게
#   -> 고급언어의 오지랖
print(id(a), id(d), id(e))
print("red", a, b[0], c[0])
test(a, b, c)
print("red", a, b[0], c[0], d, e)