from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import models, schemas, crud
from database import engine, get_db

# 테이블 자동 생성 (필요 시)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# React(3000포트)와의 통신을 위한 CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/menus", response_model=list[schemas.MenuRead])
def read_menus(db: Session = Depends(get_db)):
    return crud.get_menus(db)

@app.post("/api/menus", response_model=schemas.MenuRead)
def create_menu(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    return crud.create_menu(db=db, menu=menu)

@app.delete("/api/menus/{m_name}")
def delete_menu_api(m_name: str, db: Session = Depends(get_db)):
    # crud.py에서 정의한 삭제 로직 호출
    success = crud.delete_menu(db, m_name)
    if not success:
        raise HTTPException(status_code=404, detail="메뉴를 찾을 수 없습니다.")
    return {"message": "삭제 완료"}

