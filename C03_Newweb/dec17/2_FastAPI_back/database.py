import oracledb
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Oracle 연결 정보
DB_USER = os.getenv("DB_USER")
DB_PW = os.getenv("DB_PASSWORD")
DB_DSN = os.getenv("DB_DSN")

SQLALCHEMY_DATABASE_URL = f"oracle+oracledb://{DB_USER}:{DB_PW}@{DB_DSN}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# DB 세션 의존성 주입 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()