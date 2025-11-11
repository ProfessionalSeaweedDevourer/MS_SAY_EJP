class Seller:
    """
    판매자 정보를 담는 클래스 (DTO/VO 역할).
    MWM_SELLER 테이블의 데이터를 Python 객체로 표현합니다.
    """
    def __init__(self, name, residence, birthdate, seller_no=None):
        self.seller_no = seller_no  # 판매자 일련번호 (SELLER_NO). 조회/수정/삭제 시 사용
        self.name = name            # SELLER_NAME (판매자 이름)
        self.residence = residence       # RESIDENCE (거주지)
        self.birthdate = birthdate # BIRTH_DATE (생년월일 - 'YYYYMMDD' 형식 문자열로 유지)