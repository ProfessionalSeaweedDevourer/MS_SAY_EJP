class Doctor:
    def start(self):
        guest = self.callGuest()
        self.ask(guest)
        self.calculate(guest)
        self.tellResult(guest)

    def callGuest(self):
        return Guest()

    def ask(self, guest):
        guest.tell()

    def calculate(self):
        if guest.height > 3:
            guest.height /= 100
        guest.bmi = guest.weight / (guest.height * guest.height)

        if guest.bmi >= 39:
            guest.result = "고도비만"
        elif guest.bmi >= 32:
            guest.result = "중도비만"

    def tellResult(self):
        print("BMI: %.2f" % guest.bmi)
        print("%s 검사 결과: %s " % (guest.name, guest.result))

class Guest:
    def __init__(self):
        self.name = input("이름: ")
        self.height = input("키(m 단위): ")
        self.weight = input("체중(kg 단위): ")

    def tell(self):
        pass


###############
d = Doctor()
d.start()
