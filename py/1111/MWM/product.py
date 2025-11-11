class Product:
    """
    제품 정보를 담는 클래스 (DTO/VO 역할).
    MWM_PRODUCT 테이블의 데이터를 Python 객체로 표현합니다.
    """
    def __init__(self, name, price, category):
        self.name = name        # 제품명 (PRODUCT_NAME)
        self.price = price      # 가격 (PRICE)
        self.category = category # 상품분류 (CATEGORY)