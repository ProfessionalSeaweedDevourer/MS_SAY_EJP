from math import ceil
from seller.seller import Seller
from kwon.kwonDBManager import KwonDBManager

# 메소드 첫번째 파라메터로 self를 넣냐 마냐 - static
# 멤버변수가 없다 -> 저장할게 없다 -> 객체를 안만들어도 된다
# -> 객체를 안만들고 사용가능한 static메소드


# 총 판매자 수 파악 : DB서버랑 통신해서... -> 부담스러움 -> 횟수를 줄이자
# -> 처음 한번만 세고, 변화가 일어나면 수동 카운팅
class SellerDAO:
    def __init__(self):
        self.setAllSellerCount()  # 처음 한번만
        self.sellerPerPage = 3

    def get(self, pageNo):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.244:1521/xe")

            pageNo = int(pageNo)
            start = (pageNo - 1) * self.sellerPerPage + 1
            end = pageNo * self.sellerPerPage

            sql =  "SELECT * "
            sql += "FROM ( "
            sql += "    SELECT rownum AS rn, s_no, s_name, s_addr, s_birthday "
            sql += "    FROM ( "
            sql += "        SELECT * "
            sql += "        FROM nov11_seller "
            sql += "        ORDER BY s_name "
            sql += "    ) "
            sql += ") "
            sql += "WHERE rn >= %d AND rn <= %d" % (start, end)
            cur.execute(sql)

            sellers = []
            for _, no, name, addr, birthday in cur:
                s = Seller(no, name, addr, birthday)
                sellers.append(s)
            return sellers
        except Exception as e:
            print(e)
            return None
        finally:
            KwonDBManager.closeConCur(con, cur)

    def getAll(self):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.244:1521/xe")
            sql = "select * from nov11_seller order by s_name"
            cur.execute(sql)

            sellers = []
            for no, name, addr, birthday in cur:
                s = Seller(no, name, addr, birthday)
                sellers.append(s)
            return sellers

            # return cur
            # 1) 16번줄에서 닫아서 없어짐
            # 2) V를 작업하는 사람은 Python을 잘 모르는 사람 -> 최대한 쓰기 쉽게 만들어줘야
        except Exception as e:
            print(e)
            return None
        finally:
            KwonDBManager.closeConCur(con, cur)

    def getPageCount(self, searchTxt): # 입력 내용에 따라, '검색'할지 '조회'할지를 선택할 수 있도록 개선
        if searchTxt == "":
            sellerCount = self.allSellerCount
        else:
            sellerCount = # 검색으로 얻은 실제 판매자 수로 설정.
            pass
        return ceil(self.allSellerCount / self.sellerPerPage)

    def reg(self, seller):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.244:1521/xe")

            sql = "INSERT INTO nov11_seller "
            sql += "values(nov11_seq.nextval, '%s', '%s', to_date('%s', 'YYYYMMDD'))" % (seller.name, seller.addr, seller.birthday)

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                self.allSellerCount += 1    # 등록 성공하면 allSellerCount 수동으로 1씩 올림
                return "등록 성공"
            else:
                return "등록 실패"
        except Exception as e:
            print(e)
            return "등록 실패"
        finally:
            KwonDBManager.closeConCur(con, cur)

    def setAllSellerCount(self):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.244:1521/xe")
            sql = "select count(*) from nov11_seller"
            cur.execute(sql)

            for result in cur:
                self.allSellerCount = result[0]  # allSellerCount라는 멤버변수에 8세팅

        except Exception as e:
            print(e)
        finally:
            KwonDBManager.closeConCur(con, cur)
