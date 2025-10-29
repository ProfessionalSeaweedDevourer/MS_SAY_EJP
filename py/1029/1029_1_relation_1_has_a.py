# 클래스 간 관계 개념의 확장. has a / is a - 부분집합.

# 연습: 제품명 모나미 153, 가격이 500인 상품

# --------------------------------------------------------------------------------------------------------------------------------------

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def printProdInfo(self):
        print(f"제품명: {self.name} / 가격: \\ {self.price}")

# --------------------------------------------------------------------------------------------------------------------------------------

# pen_1 = Product("모나미 153", 500) 
# pen_1.printProdInfo()

# "Pen IS A Product" - 이 관계가 성립하면 '상속' 할 수 있다.

class Pen(Product): # 이를 통해 Pen은 Product로부터 상속된다. Product는 Super / 상위 / 부모 클래스이다.
                    # Python의 상속은 이렇게 class 하위클래스(상위클래스)로 정의한다.
                    # 대표적인 다른 언어인 java에서는, public class Pen extends Product 로 정의한다.
    pass

p1 = Pen("모나미 153", 500)
p1.printProdInfo() # 생성자도, 메서드도 없는 빈 클래스 Pen에서도 '상속'된 기능을 그대로 쓸 수 있다.

# --------------------------------------------------------------------------------------------------------------------------------------

# 실습: '우유' / 서울우유 1L / 3000

class Milk(Product): # 우유에는 '유통기한' 개념이 있다. 우유 클래스만의 기능으로 이를 추가해 보자.
                     # 다른 언어들은 보통 '생성자까지 상속'해 주지는 않는데, python은 멤버 변수를 생성자에서 결정해 버린다.

    def __init__(self, name, price, exp): # 기존 속성에 더해 새로운 속성 exp를 추가한다.
        super().__init__(name, price) # 상위 클래스에 있던 name과 price는 상위 클래스의 생성자를 그대로 활용한다.
        self.exp = exp # Milk만의 속성인 exp는 이렇게 받는다.

    # 이와 같은 'python의 생성자 상속'은 어떻게 설명할 수 있는가?
    # '같은 이름의 메서드'에 '기능을 추가'한다는 점에서 굳이 고르자면 override에 가깝다.

# --------------------------------------------------------------------------------------------------------------------------------------

    # Product 내의 printProdInfo()에서는, 'Milk 내에만 존재하는' 속성 exp를 출력할 수 없다.
    # 이와 같은 경우 override하여 해결한다.

    def printProdInfo(self): # 같은 이름의 메서드를 만들고 >
        super().printProdInfo() # 기존 기능은 그대로 물려받는다.
        print(self.exp)         # 그 후, 새로 추가할 기능을 넣는다.

    # * override VS. overload:
    #   > override: 상속 관계의 클래스에서, 부모 클래스에 이미 있는 메서드를 자식 클래스에서 재정의, 함수의 기능을 수직적 확장.
    #   > overload: 동일한 이름의 여러 개 함수를 만들어, 매개변수에 따른 함수의 데이터 처리 유연성을 수평적 확장.

seoulmilk = Milk("서울우유 1L", 3000, "11월 1일")
seoulmilk.printProdInfo()

# --------------------------------------------------------------------------------------------------------------------------------------

# 실습: 품명 조던123, 가격 150000, 사이즈 270인 신발을 만들자.

class Shoes(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size # 사실 size = None으로 미개하게 만들어도 상관없다.

    def printProdInfo(self):
        super().printProdInfo()
        print(self.size)

jordan123 = Shoes("조던123", 150000, 270)
jordan123.printProdInfo()

# --------------------------------------------------------------------------------------------------------------------------------------

# 실습: 데스크탑

class Desktop(Product):
    def __init__(self, name, price, cpu, ram, disk):
        super().__init__(name, price)
        self.cpu = cpu
        self.ram = ram
        self.disk = disk

    def printProdInfo(self):
        super().printProdInfo()
        print(self.cpu, self.ram, self.disk)

ms123 = Desktop("매직스테이션123", 2000000, "i7-1234", 32, 500)
ms123.printProdInfo()

# --------------------------------------------------------------------------------------------------------------------------------------

# 실습: 상속의 상속 - '다단상속'

class Laptop(Desktop):
    def __init__(self, name, price, cpu, ram, disk, weight):
        super().__init__(name, price, cpu, ram, disk)
        self.weight = weight

    def printProdInfo(self):
        super().printProdInfo()
        print(f"{self.weight}kg")

gram123 = Laptop("그램123", 2500000, "i7-5678", 32, 1000, 3)
gram123.printProdInfo()