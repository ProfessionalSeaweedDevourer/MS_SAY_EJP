import pandas as pd
import oracledb

# 1. 접속 정보 설정
db_config = {
    "user": "ericjpark",
    "password": "0000",
    "dsn": "195.168.9.99:1521/xe"
}

try:
    # 2. Oracle DB 연결
    conn = oracledb.connect(
        user=db_config["user"],
        password=db_config["password"],
        dsn=db_config["dsn"]
    )
    
    # 3. SQL 쿼리 작성 (예: 전체 데이터 조회)
    query = "SELECT * FROM users" # 실제 테이블 명으로 수정하십시오.
    
    # 4. Pandas를 이용해 SQL 결과를 바로 데이터프레임으로 로드
    df = pd.read_sql(query, conn)
    
    print("--- DB 로드 결과 ---")
    print(df.head())
    
    # 연결 종료
    conn.close()

except oracledb.Error as e:
    print(f"Oracle DB 연결 오류 발생: {e}")