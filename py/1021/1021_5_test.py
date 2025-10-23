# call by value vs call by reference: python은 후자만 존재
def test(a, b, c):
    print("Green", a, b[0], c[0])
    a = 100
    b[0] = 100 # b[0]은 영구적으로 100으로 재설정됨
    c = [100, 200] # c를 (여기에서만) 별도의 객체에 연결함
    global e # 전역 변수 사용 선언: 이 시점부터 e는 기존의 e임
    print("Green", a, b[0], c[0])
    
    


a = 10
b = [10, 20]
c = [10, 20]
print("Red", a, b[0], c[0])  # Red 10 10 10
test(a, b, c)  # Green 10 10 10 / Green 100 100 100
print("Red", a, b[0], c[0])  # Red 10 100 100 < 10 100 10임. 마지막 c: 함수 밖에서는 기존의 c에 연결되어 있음

