from product.productDAO import ProductDAO
from seller.sellerDAO import SellerDAO
from consoleScreen import ConsoleScreen

# 혼자만 사용x, 쇼핑몰 직원들이(1000명) 같이 사용
# -> DB계정 하나를 여럿이 사용
# 계정 하나를 동시에 사용가능한 사람 수는 정해져있음(100명)
# -> 계정을 빨리 쓰고 빨리 끊어야, 1000명이 다 사용가능


if __name__ == "__main__": # 이 if문 뭐지 - import
    sellerDAO = SellerDAO()

    while True:
        menu = ConsoleScreen.showMainMenu()

        if menu == "10":
            break
        elif menu == "1":
            seller = ConsoleScreen.showRegSellerMenu()
            result = sellerDAO.reg(seller)
            ConsoleScreen.showResult(result)
        elif menu == "2":
            product = ConsoleScreen.showRegProductMenu()
            result = ProductDAO.reg(product)
            ConsoleScreen.showResult(result)
        elif menu == "3":
            sellers = sellerDAO.getAll()
            ConsoleScreen.showSellers(sellers)
        elif menu == "4":
            products = ProductDAO.getAll()
            ConsoleScreen.showProducts(products)
        elif menu == "5":
            pageCount = sellerDAO.getPageCount()
            pageNo = ConsoleScreen.showSelectPageNoMenu(pageCount)
            sellers = sellerDAO.get(pageNo)
            ConsoleScreen.showSellers(sellers)