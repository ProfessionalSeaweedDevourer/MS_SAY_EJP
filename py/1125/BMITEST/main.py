# main.py

from fastapi import FastAPI, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import shutil
import uuid
from starlette.responses import JSONResponse

app = FastAPI()

origins = ["*"] # 모든 출처 허용 (테스트용)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

UPLOAD_DIR = Path("static/uploaded_photos")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True) # 폴더가 없으면 생성

@app.post("/calculate-and-upload")
async def calculate_and_upload(
    name: str = Form(...),
    height: float = Form(...),
    weight: float = Form(...),
    stdWeight: str = Form(...), 
    bmi: str = Form(...),       
    judgment: str = Form(...),  
    photo: UploadFile = None
):

    photo_path = None
    if photo and photo.filename:
        # 파일명 중복 방지를 위한 고유 UUID 사용
        file_extension = Path(photo.filename).suffix
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        file_location = UPLOAD_DIR / unique_filename
        
        # 파일 저장
        with file_location.open("wb") as buffer:
            shutil.copyfileobj(photo.file, buffer)
        photo_path = f"/static/uploaded_photos/{unique_filename}" 

    # JS에서 받은 모든 결과와 파일 경로를 JSON 형태로 클라이언트에 반환
    return JSONResponse(content={
        "name": name,
        "weight": weight,
        "stdWeight": stdWeight,
        "bmi": bmi,
        "judgment": judgment,
        "photo_path": photo_path
    })