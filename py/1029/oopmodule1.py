class Mouse:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(self.name, self.price)

# 외부 클래스 임포트 예제
from oopmodule2 import Book

b = Book("점프투파이썬", 30000)
b.show()

