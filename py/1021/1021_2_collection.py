# python만의 개념: range - 범위 표현, 규칙적인 list, 
a = range(10) # 0 - 9
a = range(2, 10) # 2 - 9
a = range(2, 10, 3) # 2 - 9를 3칸씩

print(a)
print(type(a))

# 1 - 389734298까지 가는 list를 만들려면...답이 없음
# 여기서 range 생성 > list 변환을 활용

b = range(1, 21)
b = list(b) # 일단 range로 만들고 list로 변환
print(b)
print(type(b))

# tuple: list와 같은 특징을 지녔지만, 데이터 표현 용도가 아님. python만의 특수 문법 기반
c = (10, 10, 30, 2, 50)
print(c)
print(type(c))
print(c[2])

x = 10
y = 20

(x,y) = (y,x) # tuple을 활용한 스왑 구현

print(x)
print(y)

# 또 다른 튜플 활용 예제

q = 100
w = 200
e = 300
(q, w, e) = (w, e, q)
print(q)
print(w)
print(e)