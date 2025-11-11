from product.product import Product
from seller.seller import Seller


class ConsoleScreen:
    def showMainMenu():  
        print("1) 판매자 등록")
        print("2) 상품 등록")
        print("3) 전체 판매자 조회")
        print("4) 전체 상품 조회")
        print("5) 판매자 조회")
        print("...")
        print("10) 종료")
        print("-----")
        return input("뭐 : ")
    
    def showProducts(products):
        for product in products:
            print(product.no)
            print(product.name)
            print(product.price)
            print(product.cate)
            print(product.s_no)
            print("-----")

    def showRegProductMenu():
        name = input("상품명 : ")
        price = input("가격 : ")
        cate = input("카테고리 : ")
        s_no = input("판매자 번호 : ")
        return Product(None, name, price, cate, s_no)

    def showRegSellerMenu():
        name = input("판매자명 : ")
        addr = input("판매자 집 주소 : ")
        birthday = input("판매자 생일 : ")
        return Seller(None, name, addr, birthday)

    def showResult(result):
        print(result)
        print("-----")

    def showSelectPageNoMenu(pageCount):
        return input("페이지(1 ~ %d) : " % pageCount)

    def showSellers(sellers):
        for seller in sellers:
            print(seller.no)
            print(seller.name)
            print(seller.addr)
            print(seller.birthday)
            print("-----")
