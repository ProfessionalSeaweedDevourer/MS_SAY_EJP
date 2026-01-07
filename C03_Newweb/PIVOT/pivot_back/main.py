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


@app.post("/login", response_model=schemas.LoginResponse)
def login_user(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    # 사용자 조회
    db_user = db.query(models.User).filter(models.User.id == user.id).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="아이디 또는 비밀번호가 일치하지 않습니다.")

    # 간단한 응답: id와 표시용 name, 선택적 프로필 정보 포함
    return {
        "id": db_user.id,
        "name": db_user.id,
        "birth_date": db_user.birth_date,
        "address": db_user.address,
    }


@app.get("/users/{user_id}", response_model=schemas.LoginResponse)
def get_user(user_id: str, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")

    return {
        "id": db_user.id,
        "name": db_user.name or db_user.id,
        "birth_date": db_user.birth_date,
        "address": db_user.address,
        "role": db_user.role,
        "description": db_user.description,
    }


@app.put("/users/{user_id}", response_model=schemas.LoginResponse)
def update_user(user_id: str, payload: schemas.UserUpdate, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")

    # Update allowed fields
    if payload.name is not None:
        db_user.name = payload.name
    if payload.role is not None:
        db_user.role = payload.role
    if payload.description is not None:
        db_user.description = payload.description

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {
        "id": db_user.id,
        "name": db_user.name or db_user.id,
        "birth_date": db_user.birth_date,
        "address": db_user.address,
        "role": db_user.role,
        "description": db_user.description,
    }