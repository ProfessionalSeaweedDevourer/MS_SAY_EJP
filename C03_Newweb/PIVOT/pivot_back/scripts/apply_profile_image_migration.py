from sqlalchemy import text
from database import engine

CHECK_SQL = "SELECT COUNT(*) AS CNT FROM user_tab_columns WHERE table_name='USERS' AND column_name='PROFILE_IMAGE_MIME'"
ALTER_SQL = "ALTER TABLE users ADD (profile_image_filename VARCHAR2(255), profile_image_mime VARCHAR2(100))"

def main():
    with engine.connect() as conn:
        try:
            cnt = conn.execute(text(CHECK_SQL)).scalar()
            if cnt and int(cnt) > 0:
                print('컬럼이 이미 존재합니다. 아무 작업도 수행하지 않습니다.')
                return

            print('컬럼이 없어 추가합니다...')
            conn.execute(text(ALTER_SQL))
            conn.commit()
            print('마이그레이션이 완료되었습니다: profile_image_filename, profile_image_mime 컬럼이 추가되었습니다.')
        except Exception as e:
            print('오류 발생:', e)

if __name__ == '__main__':
    main()
