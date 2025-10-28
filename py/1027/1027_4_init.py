# 컴퓨터 스펙

class PC:

    def __init__(self, cpu, ram, hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    def showPCInfo(self):
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.ram}")
        print(f"디스크: {self.hdd}")
        print("------------------")

myPC = PC("i7-1234", 16, 250)
myPC.showPCInfo()

# 실습: 펜으로 다시 하기

class Pen:
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
    
    def showPenInfo(self):
        print(f"{self.model} / {self.color} / {self.price}")

myPen = Pen("모나미 153", "Black", 500)
myPen.showPenInfo()