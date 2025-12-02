class Avenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print(f"본명: {self.name} / 연령: {self.age}")

    def attack(self):
        print("공격")

# --------------------------------------------------------------------------------------------------------------------------------------

class Human:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def eat(self):
        print("쿰척")

    def printInfo(self):
        print(f"이름: {self.name} / 주소지: {self.address}")

# --------------------------------------------------------------------------------------------------------------------------------------
# 아이언맨은 '존재'한다.
# 어벤저스는 '개념'이다. 분류는 근본적으로 추상적이다.

class Ironman(Avenger, Human):
# 아이언맨은 어벤저이자 인간이다. > '다중상속'이 발생한다.
# 대부분 안 되는데 아무튼 python은 됨.

    def __init__(self, name, age, agent, address):
        super().__init__(name, age) # Ironman의 super는 먼저 나온 Avenger로 지정되어 있다.
        self.agent = agent
        self.address = address # 이럴 거면 상속의 의미가...

    def printInfo(self): 
        super().printAvengerInfo()
        print(self.agent)

    def attack(self):
        print("리펄서 빔")

tstark = Ironman("Tony", 40, "JARVIS")
tstark.attack()
tstark.printInfo()

# --------------------------------------------------------------------------------------------------------------------------------------



