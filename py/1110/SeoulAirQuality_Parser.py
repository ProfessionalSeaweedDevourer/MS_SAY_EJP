import xml.etree.ElementTree as ET
from http.client import HTTPConnection
import pandas as pd
import os
import datetime
import oracledb
from oracledb import connect

# 1. API 통신 및 resBody 획득
host = "openapi.seoul.go.kr"
port = 8088
url_path = "/***REMOVED_SEOUL_KEY***/xml/RealtimeCityAir/1/25/" 
resBody = None

try:
    hc = HTTPConnection(host, port)
    hc.request("GET", url_path)
    res = hc.getresponse()
    
    if res.status == 200:
        resBody = res.read()
    else:
        print(f"오류 발생: HTTP 상태 코드 {res.status}")
        print(res.read().decode())
        
    hc.close()

except Exception as e:
    print(f"통신 중 오류 발생: {e}")

# 2. XML 파싱 및 데이터 추출
data_list = []
if resBody:
    seoulDustData = ET.fromstring(resBody) 
    row_s = seoulDustData.iter("row")
    
    for r in row_s:
        msrmt_raw = r.find('MSRMT_DT').text if r.find('MSRMT_DT') is not None else 'N/A'
        
        extracted_data = {
            '측정일시': msrmt_raw, 
            '권역명': r.find('SAREA_NM').text if r.find('SAREA_NM') is not None else 'N/A',
            '측정소명': r.find('MSRSTN_NM').text if r.find('MSRSTN_NM') is not None else 'N/A',
            'PM': r.find('PM').text if r.find('PM') is not None else 'N/A',
            'FPM': r.find('FPM').text if r.find('FPM') is not None else 'N/A',
            '통합등급': r.find('CAI_IDX').text if r.find('CAI_IDX') is not None else 'N/A'
        }
        data_list.append(extracted_data)

# --------------------------------------------------
# 3. DB에 데이터 삽입 (수정된 컬럼명 반영)
# --------------------------------------------------
if data_list:
    
    con = None
    cur = None
    
    try:
        con = connect("ericjpark/0000@195.168.9.249:1521/xe")
        cur = con.cursor()

        table_name = "SEOUL_AIR_QUALITY"
        
        # 1) 기존 테이블이 있으면 삭제 (개발/테스트용)
        try:
            cur.execute(f"DROP TABLE {table_name}")
            print(f"기존 테이블 {table_name} 삭제 완료.")
        except oracledb.Error as e:
            if len(e.args) > 0 and hasattr(e.args[0], 'code') and e.args[0].code == 942:
                print(f"테이블 {table_name}이 존재하지 않아 삭제를 건너뜜.")
            else:
                raise 
                
        # 2) 테이블 생성 (✨새로운 컬럼명 반영✨)
        create_sql = f"""
        CREATE TABLE {table_name} (
            saq_date    VARCHAR2(20)    NOT NULL,
            saq_area    VARCHAR2(50),
            saq_district VARCHAR2(50)    NOT NULL,
            saq_pm10    NUMBER(10, 2),
            saq_pm25    NUMBER(10, 2),
            saq_score   VARCHAR2(10),
            CONSTRAINT PK_{table_name} PRIMARY KEY (saq_date, saq_district) 
        )
        """
        cur.execute(create_sql)
        print(f"새 테이블 {table_name} 생성 완료.")


        # ✨INSERT 쿼리에도 새로운 컬럼명 반영✨
        insert_sql = "INSERT INTO SEOUL_AIR_QUALITY (saq_date, saq_area, saq_district, saq_pm10, saq_pm25, saq_score) VALUES (:1, :2, :3, :4, :5, :6)"
        
        # 삽입할 데이터 리스트 (튜플의 리스트) 생성
        data_to_insert = [
            (
                d['측정일시'], 
                d['권역명'], 
                d['측정소명'], 
                float(d['PM']) if d['PM'] not in ['N/A', None] and d['PM'].replace('.', '', 1).isdigit() else None, 
                float(d['FPM']) if d['FPM'] not in ['N/A', None] and d['FPM'].replace('.', '', 1).isdigit() else None, 
                d['통합등급']
            ) for d in data_list
        ]
        
        # executemany를 이용한 대량 삽입
        cur.executemany(insert_sql, data_to_insert)
        con.commit()
        
        print(f"\n✅ DB 삽입 완료: 총 {cur.rowcount}개 레코드가 삽입되었습니다.")
        
    except oracledb.Error as db_e:
        print(f"\n❌ 데이터베이스 오류 발생: {db_e}")
        if con:
            con.rollback()
    except Exception as e:
        print(f"\n❌ DB 처리 중 일반 오류 발생: {e}")
        if con:
            con.rollback()
    finally:
        if cur:
            cur.close()
        if con:
            con.close()

# --------------------------------------------------
# 4. 중복 제거 및 CSV 저장
# --------------------------------------------------
if data_list:
    df_new = pd.DataFrame(data_list)
    
    csv_file_name = "seoul_air_quality_data.csv"
    key_cols = ['측정일시', '측정소명'] # CSV 저장은 기존 컬럼명 유지 (DB 삽입과 별개)
    
    if os.path.isfile(csv_file_name):
        # 4-1. 파일이 존재하면 기존 데이터 로드
        df_old = pd.read_csv(csv_file_name, encoding='utf-8-sig')
        
        # 기존 데이터의 키 컬럼을 문자열로 통일 (타입 불일치 문제 해결)
        df_old[key_cols] = df_old[key_cols].astype(str)
        
        # 4-2. 기존 데이터에 포함되지 않은 '새로운' 행만 필터링
        old_keys = set(df_old.apply(lambda row: tuple(row[col] for col in key_cols), axis=1))
        
        is_new = df_new.apply(lambda row: tuple(row[col] for col in key_cols) not in old_keys, axis=1)
        df_to_save = df_new[is_new]
        
        print(f"\n기존 파일에 {len(df_old)}개 레코드 존재.")
        print(f"새로 가져온 {len(df_new)}개 레코드 중, {len(df_to_save)}개 레코드만 신규 데이터입니다.")
        
    else:
        df_to_save = df_new
    
    
    # 5. 신규 데이터만 CSV에 추가 저장
    if not df_to_save.empty:
        file_exists = os.path.isfile(csv_file_name) 
        
        df_to_save.to_csv(
            csv_file_name, 
            mode='a', 
            header=not file_exists, 
            index=False, 
            encoding='utf-8-sig'
        )
        print(f"\n--- CSV 저장 완료 ---")
        print(f"'{csv_file_name}' 파일에 {len(df_to_save)}개의 신규 레코드를 추가했습니다.")
    else:
        print("\n--- CSV 저장 완료 ---")
        print("기존 파일에 이미 존재하는 데이터이므로 CSV에 추가된 레코드가 없습니다.")

import time
time.sleep(5)