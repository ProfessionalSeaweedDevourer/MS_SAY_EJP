# model/catDao.py (수정)

import oracledb
from ejp_lib.ejpDBManager import ejpDBManager
from model.category import Category

class CatDAO:
    def __init__(self):
        pass

    def insertCategory(self, category):
        """새로운 분류를 DB에 삽입 (Create)"""
        con, cur = ejpDBManager.makeConCur()
        if con is None: return 0

        sql = """
            INSERT INTO My_Category (Cat_ID, Cat_Name)
            VALUES (My_Category_Seq.NEXTVAL, :name)
        """
        
        try:
            cur.execute(sql, name=category.get_cat_name())
            con.commit()
            return 1
        except oracledb.Error as e:
            con.rollback()
            error, = e.args
            print(f"분류 삽입 오류 발생: {error.message}")
            return 0
        finally:
            ejpDBManager.closeConCur(con, cur)

    def selectAllCategories(self):
        """모든 분류 정보를 조회 (Read All)"""
        con, cur = ejpDBManager.makeConCur()
        if con is None: return []
            
        sql = "SELECT Cat_ID, Cat_Name FROM My_Category ORDER BY Cat_ID"
        categories = []
        
        try:
            cur.execute(sql)
            rows = cur.fetchall()
            
            for row in rows:
                cat = Category(cat_id=row[0], cat_name=row[1])
                categories.append(cat)
                
            return categories
        except oracledb.Error as e:
            error, = e.args
            print(f"분류 조회 오류 발생: {error.message}")
            return []
        finally:
            ejpDBManager.closeConCur(con, cur)

    def updateCategory(self, category):
        """분류 정보 수정 (Update)"""
        con, cur = ejpDBManager.makeConCur()
        if con is None: return 0

        sql = "UPDATE My_Category SET Cat_Name = :name WHERE Cat_ID = :id"
        
        try:
            cur.execute(sql, name=category.get_cat_name(), id=category.get_cat_id())
            con.commit()
            return cur.rowcount
        except oracledb.Error as e:
            con.rollback()
            print(f"분류 수정 오류: {e.args[0].message}")
            return 0
        finally:
            ejpDBManager.closeConCur(con, cur)

    def deleteCategory(self, cat_id):
        """분류 삭제 (Delete)"""
        con, cur = ejpDBManager.makeConCur()
        if con is None: return 0

        sql = "DELETE FROM My_Category WHERE Cat_ID = :cat_id"
        
        try:
            cur.execute(sql, cat_id=cat_id)
            con.commit()
            return cur.rowcount
        except oracledb.Error as e:
            con.rollback()
            print(f"분류 삭제 오류: {e.args[0].message}")
            return 0
        finally:
            ejpDBManager.closeConCur(con, cur)