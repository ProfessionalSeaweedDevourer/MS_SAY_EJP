from product.product import Product
from kwon.kwonDBManager import KwonDBManager

class ProductDAO:
    def getAll():
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

    def reg(product):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.244:1521/xe")

            sql =  "INSERT INTO nov11_product "
            sql += "values(nov11_seq.nextval, '%s', %s, '%s', %s)" % (product.name, product.price, product.cate, product.s_no)

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return "등록 성공"
            else:
                return "등록 실패"
        except Exception as e:
            print(e)
            return "등록 실패"
        finally:
            KwonDBManager.closeConCur(con, cur)