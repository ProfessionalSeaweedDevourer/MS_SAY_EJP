# python의 데이터는 기본적으로 모두 객체.

s = "Sampletextstring" # 원래대로라면 s = str("Sampletextstring")으로 정의해야 했을 것.
print(s)
print(type(s))
print(id(s))

# polymorphism(다형성): '상위' 자료형에 '하위' 자료형 넣기. python에서는 일상.
# '변수'의 자료형은 무엇일까? - python에는 사실 형변환이 없다. 변수의 기본 자료형은 object다.

s = "키\t: %.2fcm" % 180.4501923
print(s)

s = """모
            양
        그          대
            로"""
print(s)

# 주석

"""
주석?
객체가 생성되지만 변수로는 저장되지 않음.
GC에 의해 치워짐.
"""