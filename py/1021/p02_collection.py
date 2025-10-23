# range : 범위표현, 규칙적인 list
a = range(10)  # 0 ~ (10 - 1)
a = range(2, 10)  # 2 ~ (10 - 1)
a = range(2, 10, 3)  # 2 ~ (10 - 1), 3칸씩
print(a)
print(type(a))

# list 1 ~ 20
b = range(1, 21)
b = list(b)  # range -> list
print(b)
print(type(b))

# tuple : 특징은 list랑 똑같
# 데이터들 표현용x
# Python의 특수한 문법의 기반
c = (10, 10, 30, 2, 50)
print(c)
print(type(c))
print(c[2])

x = 10
y = 20
# (x, y) = (y, x)
x, y = y, x # ()생략가능
print(x)
print(y)

# (q, w, e) = (100, 200, 300) 
q, w, e = 100, 200, 300 
print(q)
print(w)
print(e)