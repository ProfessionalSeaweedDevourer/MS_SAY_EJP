# # shift 연산: 2진수 변환하고 밀기

# a = 10
# b = 12
# c = a << b
# d = a >> b
# print("%d, %d" % (c,d))

name = str(input("이름 입력: "))
# height = float(input("키 입력(cm 단위): "))
# age = int(input("나이 입력(연 단위): "))
# print("---------")
# print("키 %.1f cm, 연령 %d 세" % (height, age))

# 논리 - 비교 연산
#   > 연산자는 기본적으로 stack에서 작동
#   > 그러나, python은 데이터가 종류와 무관하게 heap에서 작동함
height = 178
age = 27

a = height > 130
print(a)

b = age < 10
# 10 > age도 동작에는 문제가 없지만 일반적으로 선호되지 않음
print(b)

c = height <= 120
print(c)

d = age == 5
print(d)

e = age != 10
print(e)

f = ((age % 2) == 1)
print(f)

g = (name == "홍길동")
print(g)

# python은 and, or를 기호 하나씩만 씀
#           and     or      not
# 표준      &&      ||      !
# python    and     or      not

h = (height >= 100 & age >= 80)
print(h)

i = (age >=90 | height >=80)
print(i)