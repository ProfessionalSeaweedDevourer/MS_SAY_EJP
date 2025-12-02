# 객체: 추상적인 '존재'. 객체를 '만들기' 위해 '클래스'라는 '틀'이 필요.

class Cat: # 다른 언어에서는 클래스명은 대문자 시작이 국룰
    name = None # 객체의 속성
    age = None

    def meow(self): # 객체의 행동: method. 클래스 내부적으로 적용되는 일종의 함수 같은 것.
                    # python 문법상 여기에는 일단 self가 들어가야 함.
                    # 프로그램상 필요한 각종 기능을 이렇게 구현  
        print("야옹")

    def showCatInfo(self):
        print(f"이름: {self.name}, 나이: {self.age}세") # '각 객체'의 속성을 지정하기 위해 'self의 속성'과 연결해 줌. 

kitty1 = Cat() # 정해진 속성들을 갖는 cat 하나를 만들어, kitty라는 이름으로 저장.
kitty1.name = "루나" # '틀'에 맞게 찍어내고, 각 속성의 값을 지정.
kitty1.age = 2
kitty1.meow()
kitty1.showCatInfo()

kitty2 = Cat()
kitty2.name = "나루"
kitty2.age = 4
kitty2.meow()
kitty2.showCatInfo()

# 전역변수와 지역변수: global / local.
# global이 붙어 있는 변수는 어디에서나 사용 가능.
# 지역변수는 정의된 함수/메소드 내에서, 진행하는 동안에만 씀
# 멤버 변수 (attribute / field)