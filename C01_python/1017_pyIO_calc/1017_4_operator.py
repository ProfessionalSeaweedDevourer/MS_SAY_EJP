# # 대입 연산자 = 의 우선순위는 가장 낮다.
x = int(input("임의의 수를 하나 입력하시오: "))
y = int(input("임의의 수를 하나 더 입력하시오: "))

print("---------------")
print("x는 %d, y는 %d" % (x, y))

# a=x+y
# b=x-y
# c=x*y
# d=x/y
#   > python에서는 int간의 나눗셈이 실수로 나온다.
#   > 무조건 값이 정수가 되게 하려면, /가 아니라 //로 연산.
# e=x%y
# print(a,b,c,d,e)

yy = "ㅎ"
zz = "ㅋ"
xx = yy + zz
print(xx)

# ww=x+zz
# print(ww)
# 다른 언어에서는 str+int 연산이 가능하다.

vv = zz * x
print(vv)
# python에 한해, str의 곱하기 연산은 반복으로 기능한다.
