# 외부 클래스 임포트 예제

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def show(self):
        print(self.title, self.price)

from oopmodule1 import Mouse

m1 = Mouse("Logitech G102", 12000)
m1.show()
# 상호 import는 금기! 소스 전체를 가져오기 때문에 루프가 발생한다.