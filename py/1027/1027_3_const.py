# 스마트폰 클래스를 이용해 내 폰을 표현하기

class Mobile:
    modelName = None
    contact = None
    price = None

    def showMobileInfo(self):
        print(f"기종: {self.modelName}")
        print(f"번호: {self.contact}")
        print(f"가격: \\ {self.price}")

myphone = Mobile()
myphone.modelName = "iPhone 13 mini"
myphone.contact = "010-4655-9347"
myphone.price = 950000

myphone.showMobileInfo()

