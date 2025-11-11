from ejp.ejpDBManager import ejpDBManager

class CompanyDAO:
    def reg(company):
        con, cur = ejpDBManager.makeConCur("ericjpark/0000@195.168.9.71:1521/xe")
        sql = "INSERT INTO 회사 "
        sql += "VALUES('%s', '%s', '%s', %d) " % (company.name, company.addr, company.ceo, company.emp)
        cur.execute(sql)

        if cur.rowcount == 1:
            con.commit()
            ejpDBManager.closeConCur(con, cur)
            return "등록 성공."
        else:
            ejpDBManager.closeConCur(con, cur)
            return "등록 실패."