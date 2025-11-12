from math import ceil
from product.product import Product
from kwon.kwonDBManager import KwonDBManager
 
class ProductDAO:
    def __init__(self):
        self.setAllProductCount()
        self.productPerPage = 3
 
    def get(self, pageNo):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.244:1521/xe")
 
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.productPerPage + 1
            end = pageNo * self.productPerPage
 
            sql =  "SELECT * "
            sql += "FROM ( "
            sql += "    SELECT rownum AS rn, p_no, p_name, p_price, p_cate, p_s_no "
            sql += "    FROM ( "
            sql += "        SELECT * "
            sql += "        FROM nov11_product "
            sql += "        ORDER BY p_name, p_price "
            sql += "    ) "
            sql += ") "
            sql += "WHERE rn >= %d AND rn <= %d" % (start, end)
            cur.execute(sql)
 
            products = []
            for _, no, name, price, cate, s_no in cur:
                p = Product(no, name, price, cate, s_no)
                products.append(p)
            return products
        except Exception as e:
            print(e)
            return None
        finally:
            KwonDBManager.closeConCur(con, cur)
 
    def getAll(self):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.244:1521/xe")
            sql = "select * from nov11_product order by p_name, p_price"
            cur.execute(sql)
 
            products = []
            for no, name, price, cate, s_no in cur:
                p = Product(no, name, price, cate, s_no)
                products.append(p)
            return products
        except Exception as e:
            print(e)
            return None
        finally:
            KwonDBManager.closeConCur(con, cur)
 
    def getPageCount(self):
        return ceil(self.allProductCount / self.productPerPage)
 
    def reg(self, product):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.244:1521/xe")
 
            sql =  "INSERT INTO nov11_product "
            sql += "values(nov11_seq.nextval, '%s', %s, '%s', %s)" % (product.name, product.price, product.cate, product.s_no)
 
            cur.execute(sql)
 
            if cur.rowcount == 1:
                con.commit()
                self.allProductCount += 1
                return "등록 성공"
            else:
                return "등록 실패"
        except Exception as e:
            print(e)
            return "등록 실패"
        finally:
            KwonDBManager.closeConCur(con, cur)
 
    def setAllProductCount(self):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.244:1521/xe")
            sql = "select count(*) from nov11_product"
            cur.execute(sql)
 
            for result in cur:
                self.allProductCount = result[0]
        except Exception as e:
            print(e)
        finally:
            KwonDBManager.closeConCur(con, cur)