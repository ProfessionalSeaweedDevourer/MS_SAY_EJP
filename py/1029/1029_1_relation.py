# 클래스 간 관계 개념의 확장. has a / is a - 부분집합.

# 연습: 제품명 모나미 153, 가격이 500인 상품


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def printProdInfo(self):
        print(f"제품명: {self.name} / 가격: \\ {self.price}")

# pen_1 = Product("모나미 153", 500) 
# pen_1.printProdInfo()

# "Pen IS A Product" - 이 관계가 성립하면 '상속' 할 수 있다.

class Pen(Product): # 이를 통해 Pen은 Product로부터 상속된다. Product는 Super / 상위 / 부모 클래스이다.
                    # Python의 상속은 이렇게 class 하위클래스(상위클래스)로 정의한다.
                    # 대표적인 다른 언어인 java에서는, public class Pen extends Product 로 정의한다.
    pass

p1 = Pen("모나미 153", 500)
p1.printProdInfo() # 생성자도, 메서드도 없는 빈 클래스 Pen에서도 '상속'된 기능을 그대로 쓸 수 있다.

# 실습: '우유' / 서울우유 1L / 3000

class Milk(Product): # 우유에는 '유통기한' 개념이 있다. 우유 클래스만의 기능으로 이를 추가해 보자.
                     # 다른 언어들은 보통 '생성자까지 상속'해 주지는 않는데, python은 멤버 변수를 생성자에서 결정해 버린다.

    def __init__(self, name, price, exp): # 기존 속성에 더해 새로운 속성 exp를 추가한다.
        super().__init__(name, price) # 상위 클래스에 있던 name과 price는 상위 클래스의 생성자를 그대로 활용한다.
        self.exp = exp # Milk만의 속성인 exp는 이렇게 받는다.

    # 여기서 문제는, Product 내의 printProdInfo()에서 'Milk 내에만 존재하는' 속성 exp를 출력하는 것.
    # 이와 같은 경우 override하여 해결한다.

    def printProdInfo(self): # 같은 이름의 메서드를 만들고 >
        super().printProdInfo() # 기존 기능은 그대로 물려받는다.
        print(self.exp)         # 그 후, 새로 추가할 기능을 넣는다.

    # * override VS. overload:
    #   > override: 상속 관계의 클래스에서, 부모 클래스에 이미 있는 메서드를 자식 클래스에서 재정의, 함수의 기능을 수직적 확장.
    #   > overload: 동일한 이름의 여러 개 함수를 만들어, 매개변수에 따른 함수의 데이터 처리 유연성을 수평적 확장.

seoulmilk = Milk("서울우유 1L", 3000, "11월 1일")
seoulmilk.printProdInfo()