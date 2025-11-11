from mwmDAO import MWMDAO
from consoleScreen import ConsoleScreen

if __name__ == "__main__":
    # ConsoleScreen.getInfo()가 반환하는 seller, product 두 객체를 언패킹하여 받습니다.
    seller, product = ConsoleScreen.getInfo()
    
    # 입력 과정에서 오류가 발생하여 None이 반환되었는지 확인
    if seller is None or product is None:
        ConsoleScreen.printResult("입력 데이터가 유효하지 않아 작업을 중단합니다.")
    else:
        # CompanyDAO는 이제 인스턴스 메서드를 사용하므로, 객체를 생성합니다.
        dao = MWMDAO()
        
        # DAO의 개선된 메서드(reg_seller_and_product)를 호출합니다.
        result = dao.reg(seller, product)
        
        # 결과 출력
        ConsoleScreen.printResult(result)