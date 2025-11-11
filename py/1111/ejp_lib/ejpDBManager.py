# ejpDBManager.py

import oracledb

class ejpDBManager:
    @staticmethod
    def makeConCur(connect_string):
        try:
            con = oracledb.connect(connect_string)
            cur = con.cursor()
            return con, cur
        except oracledb.Error as e:
            error, = e.args
            print(f"데이터베이스 연결 오류 발생: {error.message}")
            return None, None

    @staticmethod
    def closeConCur(con, cur):
        if cur:
            try:
                cur.close()
            except oracledb.Error as e:
                print(f"커서 닫기 오류: {e}")

        if con:
            try:
                con.close()
            except oracledb.Error as e:
                print(f"연결 닫기 오류: {e}")