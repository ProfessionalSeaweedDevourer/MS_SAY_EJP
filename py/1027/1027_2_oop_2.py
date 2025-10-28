# 1) 고양이의 표현


# 3) 객체를 만들기 위해 클래스 정의
class Cat:
    name = None
    age = None

    def meow(self, cnt):
        print("애옹" * cnt)


# 2) 고양이 객체 생성
c = Cat()

# 멤버 변수 접근: "객체.변수명" 형식ㄴ
c.name = "나비"
c.age = 1
c.weight = 3  # 클래스에서 정의하지 않은 속성도, python에서는 임의 추가가 가능하다.

# 메소드의 호출
Cat.meow(c, 5) # 옛날 옛적 python식 호출 (클래스.메소드(변수))
c.meow(5) # 다른 언어에서 쓰는 일반적인 스타일 (변수.메소드)

print(c.name)
print(c.age)
print(c.weight)
