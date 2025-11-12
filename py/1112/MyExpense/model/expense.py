from datetime import datetime

class Expense:
    """
    My_Exp 테이블의 레코드를 담는 데이터 객체 (VO/DTO)
    Exp_ID, Exp_Date, Exp_Item, Exp_Amount, Cat_ID 속성을 가짐.
    """
    def __init__(self, exp_id=None, exp_date=None, exp_item=None, exp_amount=None, cat_id=None):
        self._exp_id = exp_id
        # 날짜 데이터는 datetime 객체로 관리하는 것이 일반적
        if isinstance(exp_date, str):
            # 문자열 형태의 날짜를 datetime 객체로 변환 (예시 포맷)
            self._exp_date = datetime.strptime(exp_date, '%Y-%m-%d') 
        else:
            self._exp_date = exp_date
            
        self._exp_item = exp_item
        self._exp_amount = exp_amount
        self._cat_id = cat_id

    # Getter 메서드
    def get_exp_id(self):
        return self._exp_id

    def get_exp_date(self):
        return self._exp_date

    def get_exp_item(self):
        return self._exp_item

    def get_exp_amount(self):
        return self._exp_amount

    def get_cat_id(self):
        return self._cat_id

    # Setter 메서드
    def set_exp_id(self, exp_id):
        self._exp_id = exp_id

    def set_exp_date(self, exp_date):
        # setter에서도 날짜 형식 처리 로직을 포함할 수 있음
        self._exp_date = exp_date

    def set_exp_item(self, exp_item):
        self._exp_item = exp_item

    def set_exp_amount(self, exp_amount):
        self._exp_amount = exp_amount

    def set_cat_id(self, cat_id):
        self._cat_id = cat_id

    # 객체 정보를 문자열로 반환
    def __str__(self):
        # 날짜는 읽기 쉬운 포맷으로 변환하여 출력
        date_str = self._exp_date.strftime('%Y-%m-%d') if self._exp_date else "N/A"
        return f"Expense(ID: {self._exp_id}, Date: {date_str}, Item: {self._exp_item}, Amount: {self._exp_amount}, Cat_ID: {self._cat_id})"