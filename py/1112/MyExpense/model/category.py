class Category:
    """
    My_Category 테이블의 레코드를 담는 데이터 객체 (VO/DTO)
    Cat_ID, Cat_Name 속성을 가짐.
    """
    def __init__(self, cat_id=None, cat_name=None):
        self._cat_id = cat_id
        self._cat_name = cat_name

    # Getter 메서드
    def get_cat_id(self):
        return self._cat_id

    def get_cat_name(self):
        return self._cat_name

    # Setter 메서드
    def set_cat_id(self, cat_id):
        self._cat_id = cat_id

    def set_cat_name(self, cat_name):
        self._cat_name = cat_name

    # 객체 정보를 문자열로 반환 (출력 및 디버깅 용도)
    def __str__(self):
        return f"Category(ID: {self._cat_id}, Name: {self._cat_name})"