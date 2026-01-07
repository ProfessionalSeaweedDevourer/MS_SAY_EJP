from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas, database

app = FastAPI()

# React 접속 허용 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 테이블 생성 (최초 실행 시)
models.Base.metadata.create_all(bind=database.engine)

@app.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # ID 중복 체크
    db_user = db.query(models.User).filter(models.User.id == user.id).first()
    if db_user:
        raise HTTPException(status_code=400, detail="이미 등록된 아이디입니다.")
    
    # 신규 유저 저장
    new_user = models.User(
        id=user.id,
        password=user.password,
        birth_date=user.birth_date,
        address=user.address
    )
    
    db.add(new_user)
    db.commit()
    return {"id": new_user.id, "message": "회원가입 성공"}