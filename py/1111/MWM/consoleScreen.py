from seller import Seller
from product import Product 

class ConsoleScreen:
    
    @staticmethod
    def showMainMenu():
        print("\n====================")
        print("    메인 메뉴")
        print("====================")
        print("1) 판매자 등록")
        print("2) 상품 등록")
        print("...") # 임시 메뉴 항목
        print("10) 종료")
        print("--------------------")
        
        # 사용자 입력을 받아 문자열로 반환합니다.
        return input("메뉴 선택: ")
    
    @staticmethod
    def getInfo():
        print("--- 판매자 정보 입력 ---")
        seller_name = input("판매자 이름: ")
        seller_residence = input("거주지 (예: 수원): ")
        # DB의 DATE 타입에 맞게 'YYYYMMDD' 형식의 문자열로 받습니다.
        seller_birthdate = input("생년월일 (YYYYMMDD): ")

        seller = Seller(seller_name, seller_residence, seller_birthdate)

        print("\n--- 제품 정보 입력 ---")
        product_name = input("제품명: ")
        try:
            # 가격은 정수로 변환하여 Product 객체에 전달합니다.
            product_price = int(input("가격: "))
        except ValueError:
            print("오류: 가격은 유효한 숫자로 입력해야 합니다.")
            return None, None
            
        product_category = input("상품 분류 (예: 문구류): ")

        product = Product(product_name, product_price, product_category)
        
        # DAO로 전달하기 위해 판매자와 제품 객체를 튜플로 반환합니다.
        return seller, product
    
    @staticmethod
    def printResult(result):
        print("\n--- 등록 결과 ---")
        print(result)
