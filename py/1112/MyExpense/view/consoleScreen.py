# view/consoleScreen.py

from model.expense import Expense
from model.category import Category
from datetime import datetime

class ConsoleScreen:
    """
    사용자에게 정보를 표시하고 입력을 받는 View 계층 클래스
    """

    @staticmethod
    def showMainMenu():
        """메인 메뉴를 표시하고 사용자 선택을 받습니다. (최종 메뉴 반영)"""
        print("=" * 30)
        print("💰 MyExpense 소비 내역 관리 시스템")
        print("=" * 30)
        print("1) 소비 내역 등록")
        print("2) 전체 소비 내역 조회")
        print("3) 소비 내역 수정 및 삭제") # 메뉴 3 변경
        print("4) 분류 관리 (조회/등록)") # 메뉴 4 변경
        print("5) 분류 수정 및 삭제") # 메뉴 5 추가
        print("9) 프로그램 정보")
        print("0) 종료")
        print("-" * 30)
        
        while True:
            choice = input("메뉴 선택 : ").strip()
            if choice.isdigit() and 0 <= int(choice) <= 9:
                return choice
            print("❗ 올바른 메뉴 번호를 입력하십시오.")

    @staticmethod
    def showRegExpenseMenu(categories):
        """소비 내역 등록 메뉴. 날짜 입력 시 'c'를 입력하면 취소합니다."""
        print("\n--- [ 소비 내역 등록 ] ---")
        
        # 1. 날짜 입력 (취소 기능 추가)
        while True:
            date_str = input("날짜 (YYYY-MM-DD, 예: 2025-11-12, 엔터 시 오늘 날짜, 취소: c) : ")
            
            if date_str.lower() == 'c':
                return 'CANCEL', None, None, None # 취소 신호 반환

            if not date_str:
                exp_date = datetime.now().date()
                break
            try:
                exp_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                break
            except ValueError:
                print("❗ 날짜 형식이 올바르지 않습니다 (YYYY-MM-DD).")

        # 2. 항목 입력
        exp_item = input("항목/내용 : ").strip()

        # 3. 금액 입력
        while True:
            amount_str = input("금액 : ").strip()
            if amount_str.isdigit():
                exp_amount = int(amount_str)
                break
            print("❗ 금액은 숫자로만 입력해야 합니다.")

        # 4. 분류 선택 및 등록 옵션 추가
        cat_id = None
        while True:
            print("\n--- [ 분류 선택 ] ---")
            for cat in categories:
                print(f"[{cat.get_cat_id()}] {cat.get_cat_name()}")
            print("[0] 새로운 분류 등록") 
            print("-" * 15)
            
            cat_id_str = input("분류 번호 선택 (0 입력 시 새 등록) : ").strip()
            
            if cat_id_str == '0':
                return 'REGISTER_NEW', exp_date, exp_item, exp_amount
            
            if cat_id_str.isdigit():
                selected_id = int(cat_id_str)
                if any(selected_id == c.get_cat_id() for c in categories):
                    cat_id = selected_id
                    break
            
            print("❗ 목록에 있는 유효한 분류 번호를 입력하거나, 0을 눌러 새 분류를 등록하십시오.")

        return 'OK', Expense(None, exp_date, exp_item, exp_amount, cat_id)

    @staticmethod
    def showRegCategoryMenu():
        """새로운 분류명 입력을 받습니다. 'c' 입력 시 등록 취소"""
        print("\n--- [ 분류 등록 ] ---")
        cat_name = input("새로운 분류명 (취소: c) : ").strip()
        
        if cat_name.lower() == 'c':
            return None 
            
        return Category(None, cat_name)

    @staticmethod
    def showExpenses(expenses_with_cat_name):
        """조회된 소비 내역 리스트를 출력합니다."""
        if not expenses_with_cat_name:
            print("조회된 소비 내역이 없습니다.")
            return

        print("\n--- [ 전체 소비 내역 조회 ] ---")
        
        for exp_tuple in expenses_with_cat_name:
            exp = exp_tuple[0]
            cat_name = exp_tuple[1]
            
            date_str = exp.get_exp_date().strftime('%Y-%m-%d') if exp.get_exp_date() else "N/A"
            print(f"ID: {exp.get_exp_id()}")
            print(f"날짜: {date_str}")
            print(f"항목: {exp.get_exp_item()}")
            print(f"금액: {exp.get_exp_amount():,}")
            print(f"분류: {cat_name}") 
            print("-" * 30)

    @staticmethod
    def showCategories(categories):
        """조회된 분류 리스트를 출력합니다."""
        print("=" * 30) 
        if not categories:
            print("등록된 분류가 없습니다.")
            print("=" * 30)
            return
            
        print("📂 현재 등록된 분류 목록")
        print("-" * 30)
        for cat in categories:
            print(f"[{cat.get_cat_id()}] {cat.get_cat_name()}")
        print("=" * 30) 

    # --- CRUD 입력을 위한 신규 메서드 ---

    @staticmethod
    def getTargetId(item_name):
        """수정/삭제할 대상의 ID를 입력받습니다."""
        while True:
            id_str = input(f"수정/삭제할 {item_name}의 ID (취소: c) : ").strip()
            if id_str.lower() == 'c':
                return 'c'
            if id_str.isdigit():
                return int(id_str)
            print("❗ ID는 숫자로만 입력해야 합니다.")

    @staticmethod
    def showExpenseUpdateMenu(old_exp):
        """기존 정보를 보여주고 수정할 정보를 입력받습니다. (간소화)"""
        print("\n--- [ 소비 내역 수정 ] ---")
        
        print(f"현재 항목: {old_exp.get_exp_item()}")
        new_item = input("새 항목/내용 (변경 없으면 Enter) : ").strip()
        
        print(f"현재 금액: {old_exp.get_exp_amount()}")
        new_amount_str = input("새 금액 (변경 없으면 Enter) : ").strip()

        return new_item, new_amount_str

    @staticmethod
    def showCategoryUpdateMenu(old_cat):
        """기존 분류명을 보여주고 수정할 분류명을 입력받습니다."""
        print("\n--- [ 분류명 수정 ] ---")
        print(f"현재 분류명: {old_cat.get_cat_name()}")
        new_name = input("새 분류명 (변경 없으면 Enter) : ").strip()
        return new_name

    @staticmethod
    def getActionChoice(item_name):
        """수정 또는 삭제 중 선택을 받습니다."""
        while True:
            choice = input(f"{item_name}을(를) 수정(U)하시겠습니까, 삭제(D)하시겠습니까? (취소: c) : ").strip().lower()
            if choice in ['u', 'd', 'c']:
                return choice
            print("❗ U, D, c 중 하나를 입력하십시오.")

    @staticmethod
    def showResult(message):
        """처리 결과 메시지를 출력합니다."""
        print("\n--- [ 처리 결과 ] ---")
        print(message)
        print("-" * 30)

    @staticmethod
    def showRegCategoryStartMessage():
        """새 분류 등록을 시작한다는 안내 메시지 출력"""
        print("\n--- [ 새 분류 등록 시작 ] ---")    