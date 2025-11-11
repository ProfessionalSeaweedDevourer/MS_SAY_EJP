# OOP: '객체'의 행동을 '메서드'로 미리 정의
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print(self.name, self.age)

    def visitSch(self):
        print(f"{self.name}은(는) 열심히 공부했다.")
        
    def visitGroc(self):
        print(f"{self.name}은(는) 반찬거리를 샀다.")

    def visitPark(self):
        print(f"{self.name}은(는) 공원을 산책했다.")

h = Human("홍길동", 30)
h.printInfo()
h.visitSch()


# AOP: Aspect Oriented - 관점 지향.

