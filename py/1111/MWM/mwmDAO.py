from ejp_lib.ejpDBManager import ejpDBManager
import oracledb
# from configManager import ConfigManager # 실제 프로젝트에서 연결 문자열을 관리할 때 사용

class MWMDAO:

    def reg(self, seller, product):
        con, cur = ejpDBManager.makeConCur()

        if con is None or cur is None:
            return "등록 실패. 데이터베이스 연결 오류."

        try:
            # 1. 시퀀스 값을 받을 출력 바인드 변수를 준비합니다.
            seller_no_var = cur.var(oracledb.NUMBER)

            # 2. 판매자 등록 SQL: PL/SQL 블록으로 감싸 ORA-01484 오류를 회피하고 SELLER_NO를 즉시 저장합니다.
            sql_seller = """
                BEGIN
                    INSERT INTO MWM_SELLER (SELLER_NO, SELLER_NAME, RESIDENCE, BIRTH_DATE)
                    VALUES (MWM_SELLER_SEQ.NEXTVAL, :name, :residence, TO_DATE(:bdate, 'YYYYMMDD'))
                    RETURNING SELLER_NO INTO :output_no;
                END;
            """
            cur.execute(sql_seller, 
                        name=seller.name, 
                        residence=seller.residence, 
                        bdate=seller.birthdate,
                        output_no=seller_no_var)

            # 3. 반환된 SELLER_NO 값을 Python 변수에 가져옵니다.
            new_seller_no = seller_no_var.getvalue()

            # 4. 제품 등록 SQL: 방금 얻은 new_seller_no를 외래 키로 사용합니다.
            sql_product = """
                INSERT INTO MWM_PRODUCT (PRODUCT_ID, SELLER_NO, PRODUCT_NAME, PRICE, CATEGORY)
                VALUES (MWM_PRODUCT_SEQ.NEXTVAL, :seller_no, :p_name, :price, :category)
            """
            cur.execute(sql_product,
                        seller_no=new_seller_no,
                        p_name=product.name,
                        price=product.price,
                        category=product.category)

            con.commit()
            return f"등록 성공. 판매자 번호: {new_seller_no}"

        except oracledb.Error as e:
            error, = e.args
            print(f"SQL 실행 오류 발생: {error.message}")
            con.rollback()
            return "등록 실패. 트랜잭션 롤백됨."
            
        finally:
            ejpDBManager.closeConCur(con, cur)