from os import name


class Human:
    def __init__(self, name, age, pet):
        self.name = name
        self.age = age
        self.pet = pet

    def printHumanInfo(self):
        print(f"이름: {self.name} / 연령: {self.age}세")
        self.pet.printDogInfo()


class Dog:
    def __init__(self, name, breed, bug):
        self.name = name
        self.breed = breed
        self.bug = bug

    def printDogInfo(self):
        print(f"이름: {self.name} / 견종: {self.breed}")
        self.bug.printBugInfo()


# 객체 간 관계: A has a B / B has an A
#   >

# python에는 사실 기본형이 없고 모두 객체이다.


class Bug:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def printBugInfo(self):
        print(f"분류: {self.name} / 크기: {self.size}")


b1 = Bug("벼룩", "1mm")
b1.printBugInfo()

print("-"*30)

d1 = Dog("후추", "말티즈", b1)
d1.printDogInfo()

print("-"*30)

h1 = Human("홍길동", "30", d1)
h1.printHumanInfo()
