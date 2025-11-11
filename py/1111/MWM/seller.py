class Seller:
    """
    판매자 정보를 담는 클래스 (DTO/VO 역할).
    MWM_SELLER 테이블의 데이터를 Python 객체로 표현합니다.
    """
    def __init__(self, name, residence, birthdate):
        self.name = name        # SELLER_NAME (판매자 이름)
        self.addr = residence   # RESIDENCE (거주지 - DAO에서 addr로 바인딩됨)
        self.birth_date = birthdate # BIRTH_DATE (생년월일 - 'YYYYMMDD' 형식 문자열로 유지)