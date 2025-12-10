# controller/homeController.py

from view.consoleScreen import ConsoleScreen
from model.expDao import ExpDAO
from model.catDao import CatDAO

class HomeController:
    """
    프로그램의 주 실행 흐름을 제어하는 Controller 클래스.
    View와 DAO 사이의 중재자 역할.
    """
    def __init__(self):
        self._screen = ConsoleScreen()
        self._exp_dao = ExpDAO()
        self._cat_dao = CatDAO()

    def run(self):
        """
        프로그램의 메인 루프.
        """
        while True:
            menu_choice = self._screen.showMainMenu()

            if menu_choice == '1': # 소비 내역 등록
                self.registerExpense()
            elif menu_choice == '2': # 소비 내역 조회
                self.showAllExpenses()
            elif menu_choice == '3': # 소비 내역 수정 / 삭제
                self.manageExpenseCRUD() 
            elif menu_choice == '4': # 분류 조회 / 등록
                self.manageCategories()  
            elif menu_choice == '5': # 분류 수정 / 삭제
                self.manageCategoryCRUD() 
            elif menu_choice == '0': # 종료 코드
                self._screen.showResult("프로그램을 종료합니다.")
                break
            elif menu_choice == '9':
                self._screen.showResult("버전: 1.0\n최종 업데이트: 2025-11-12")
            else:
                self._screen.showResult("잘못된 메뉴 선택입니다.")

    # --- 신규 CRUD 관리 메서드 ---

    def manageExpenseCRUD(self):
        """소비 내역 수정 및 삭제 관리"""
        self._screen.showResult("\n--- [ 소비 내역 관리 시작 ] ---")
        
        action = self._screen.getActionChoice("소비 내역")
        if action == 'c':
            self._screen.showResult("소비 내역 관리를 취소했습니다.")
            return

        target_id = self._screen.getTargetId("소비 내역")
        if target_id == 'c':
            self._screen.showResult("취소했습니다.")
            return
            
        self._screen.showResult(f"소비 내역 ID {target_id}에 대한 {action.upper()} 작업을 진행합니다. (구현 필요)")
        # [TODO: 여기에 실제 DAO 조회 및 Update/Delete 로직이 들어갑니다.]
        

    def manageCategoryCRUD(self):
        """분류 수정 및 삭제 관리 (실제 구현)"""
        self._screen.showResult("\n--- [ 분류 관리 시작 ] ---")

        action = self._screen.getActionChoice("분류")
        if action == 'c':
            self._screen.showResult("분류 관리를 취소했습니다.")
            return

        target_id = self._screen.getTargetId("분류")
        if target_id == 'c':
            self._screen.showResult("취소했습니다.")
            return
            
        if action == 'd':
            # --- 삭제 로직 ---
            result = self._cat_dao.deleteCategory(target_id)
            if result == 1:
                self._screen.showResult(f"✅ 분류 ID {target_id} 삭제가 완료되었습니다.")
            else:
                self._screen.showResult(f"❌ 분류 ID {target_id}가 존재하지 않거나 삭제에 실패했습니다. (FK 참조 확인 필요)")
        
        elif action == 'u':
            # --- 수정 로직 ---
            
            # 1. 대상 분류를 조회합니다. (DAO에 ID로 조회하는 메서드가 필요하다고 가정)
            # 현재 CatDAO에 selectById 메서드가 없으므로, 모든 분류를 조회해서 찾거나, DAO에 해당 메서드를 추가해야 합니다.
            # 여기서는 편의상 DAO에 해당 메서드 (self._cat_dao.selectCategoryById(target_id))가 있다고 가정합니다.
            
            # 현재 구조 상 편의를 위해, DAO에 개별 조회 메서드가 없으므로,
            # 모든 카테고리를 조회해서 해당 ID를 찾고, VO를 생성하는 것으로 로직을 대체합니다.
            
            all_cats = self._cat_dao.selectAllCategories()
            current_cat = next((cat for cat in all_cats if cat.get_cat_id() == target_id), None)

            if current_cat is None:
                self._screen.showResult(f"❌ 분류 ID {target_id}를 찾을 수 없습니다.")
                return

            # 2. View를 통해 새 분류명을 입력받습니다.
            new_name = self._screen.showCategoryUpdateMenu(current_cat)
            
            if not new_name:
                self._screen.showResult("변경사항이 없어 수정을 취소합니다.")
                return
            
            # 3. VO 객체를 업데이트합니다.
            current_cat.set_cat_name(new_name)
            
            # 4. DAO를 호출하여 DB에 반영합니다.
            result = self._cat_dao.updateCategory(current_cat)

            if result == 1:
                self._screen.showResult(f"✅ 분류 ID {target_id} ({new_name}) 수정이 완료되었습니다.")
            else:
                self._screen.showResult("❌ 분류 수정 중 오류가 발생했습니다. (중복된 분류명 확인 필요)")

    # --- 기존 메서드 ---
    # ... (registerExpense, showAllExpenses, manageCategories, registerCategory, showAllCategories 메서드는 기존 내용 유지)
    
    def registerExpense(self):
        # ... (기존 registerExpense 내용 유지)
        categories = self._cat_dao.selectAllCategories()

        if not categories:
            self._screen.showResult("소비 내역을 등록하려면 먼저 분류를 등록해야 합니다 (메뉴 4).")
            return
            
        while True:
            result_signal, *data = self._screen.showRegExpenseMenu(categories)
            
            if result_signal == 'CANCEL':
                self._screen.showResult("소비 내역 등록이 취소되었습니다.")
                return
            
            if result_signal == 'REGISTER_NEW':
                self.registerCategory() 
                categories = self._cat_dao.selectAllCategories()
                
                if not categories:
                    self._screen.showResult("❗ 유효한 분류 목록이 없어 등록을 종료합니다.")
                    return
                
                continue 
            
            elif result_signal == 'OK':
                expense_vo = data[0]
                break
                
            else:
                return 

        result = self._exp_dao.insertExpense(expense_vo)

        if result == 1:
            self._screen.showResult("✅ 소비 내역 등록이 완료되었습니다.")
        else:
            self._screen.showResult("❌ 소비 내역 등록 중 오류가 발생했습니다.")
            
    def showAllExpenses(self):
        expenses_with_cat_name = self._exp_dao.selectAllExpenses()
        self._screen.showExpenses(expenses_with_cat_name)

    def manageCategories(self):
        self.showAllCategories() 
        self._screen.showRegCategoryStartMessage() 
        self.registerCategory()
        
    def registerCategory(self):
        category_vo = self._screen.showRegCategoryMenu()

        if category_vo is None:
            self._screen.showResult("분류 등록이 취소되었습니다.")
            return 0 

        if not category_vo.get_cat_name():
            self._screen.showResult("❗ 분류명이 입력되지 않았습니다.")
            return 0
        
        result = self._cat_dao.insertCategory(category_vo)

        if result == 1:
            self._screen.showResult(f"✅ 분류 '{category_vo.get_cat_name()}' 등록이 완료되었습니다.")
            return 1
        else:
            self._screen.showResult("❌ 분류 등록 중 오류가 발생했거나, 이미 존재하는 분류명입니다.")
            return 0
            
    def showAllCategories(self):
        categories = self._cat_dao.selectAllCategories()
        self._screen.showCategories(categories)