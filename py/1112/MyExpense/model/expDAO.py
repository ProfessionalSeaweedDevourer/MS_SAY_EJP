# model/expDao.py

import oracledb
from ejp_lib.ejpDBManager import ejpDBManager
from model.expense import Expense

class ExpDAO:
    def __init__(self):
        pass

    def insertExpense(self, expense):
        """새로운 소비 내역을 DB에 삽입 (Create)"""
        con, cur = ejpDBManager.makeConCur()
        if con is None: return 0

        sql = """
            INSERT INTO My_Exp (Exp_ID, Exp_Date, Exp_Item, Exp_Amount, Cat_ID)
            VALUES (My_Exp_Seq.NEXTVAL, :exp_dt, :item, :amount, :cat_id)
        """
        
        try:
            cur.execute(sql, 
                        exp_dt=expense.get_exp_date(), 
                        item=expense.get_exp_item(), 
                        amount=expense.get_exp_amount(), 
                        cat_id=expense.get_cat_id())
            con.commit()
            return 1
        except oracledb.Error as e:
            con.rollback()
            error, = e.args
            print(f"소비 내역 삽입 오류 발생: {error.message}")
            return 0
        finally:
            ejpDBManager.closeConCur(con, cur)

    def selectAllExpenses(self):
        """모든 소비 내역 정보를 조회 (분류명 포함, JOIN 활용)"""
        con, cur = ejpDBManager.makeConCur()
        if con is None: return []
            
        sql = """
            SELECT 
                E.Exp_ID, E.Exp_Date, E.Exp_Item, E.Exp_Amount, E.Cat_ID, C.Cat_Name 
            FROM 
                My_Exp E INNER JOIN My_Category C
            ON 
                E.Cat_ID = C.Cat_ID
            ORDER BY 
                E.Exp_Date DESC
        """
        expenses_with_cat_name = []
        
        try:
            cur.execute(sql)
            rows = cur.fetchall()
            
            for row in rows:
                exp = Expense(exp_id=row[0], exp_date=row[1], exp_item=row[2], 
                              exp_amount=row[3], cat_id=row[4])
                expenses_with_cat_name.append((exp, row[5])) 
                
            return expenses_with_cat_name
        except oracledb.Error as e:
            error, = e.args
            print(f"소비 내역 조회 오류 발생: {error.message}")
            return []
        finally:
            ejpDBManager.closeConCur(con, cur)

    def updateExpense(self, expense):
        """소비 내역 수정 (Update)"""
        con, cur = ejpDBManager.makeConCur()
        if con is None: return 0

        sql = """
            UPDATE My_Exp 
            SET Exp_Date = :exp_dt, Exp_Item = :item, Exp_Amount = :amount, Cat_ID = :cat_id
            WHERE Exp_ID = :exp_id
        """
        try:
            cur.execute(sql, 
                        exp_dt=expense.get_exp_date(), 
                        item=expense.get_exp_item(), 
                        amount=expense.get_exp_amount(), 
                        cat_id=expense.get_cat_id(),
                        exp_id=expense.get_exp_id())
            con.commit()
            return cur.rowcount
        except oracledb.Error as e:
            con.rollback()
            print(f"소비 내역 수정 오류: {e.args[0].message}")
            return 0
        finally:
            ejpDBManager.closeConCur(con, cur)

    def deleteExpense(self, exp_id):
        """소비 내역 삭제 (Delete)"""
        con, cur = ejpDBManager.makeConCur()
        if con is None: return 0

        sql = "DELETE FROM My_Exp WHERE Exp_ID = :exp_id"
        
        try:
            cur.execute(sql, exp_id=exp_id)
            con.commit()
            return cur.rowcount
        except oracledb.Error as e:
            con.rollback()
            print(f"소비 내역 삭제 오류: {e.args[0].message}")
            return 0
        finally:
            ejpDBManager.closeConCur(con, cur)