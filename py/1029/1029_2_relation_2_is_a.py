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
    def __init__(self, name, age, agent):
        super().__init__(name, age)
        self.agent = agent

# 아이언맨은 어벤저이자 인간이다. > '다중상속'이 발생한다.
# 대부분 안 되는데 아무튼 python은 됨.

    def printInfo(self):  # 다중 상속 상황에서 이름이 같은 게 '또' 나오면? > 먼저 상속받은 쪽이 적용.
        super().printAvengerInfo()
        print(self.agent)

    def attack(self):
        print("리펄서 빔")

tstark = Ironman("Tony", 40, "JARVIS")
tstark.attack()
tstark.printInfo()

# --------------------------------------------------------------------------------------------------------------------------------------



