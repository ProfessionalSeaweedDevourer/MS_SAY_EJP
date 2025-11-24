from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
import os
from uuid import uuid4

app = FastAPI()

# FastAPI의 비동기식 연결 활용,
# 클라이언트 측 상대 경로에 대상 파일을 일단 받기
@app.post("/file.upload")
async def fileUpload(photo: UploadFile, zipp:  UploadFile, title: str=Form()):
    folder2 = "./ZipFolder/"
    content2 = await zipp.read()
    filename2 = zipp.filename
    type2 = filename2[-4:]
    filename2 = filename2.replace(type2, "")
    filename2 = filename2 + "_" + str(uuid4()) + type2
    f2 = open(folder2 + filename2, "wb")
    f2.write(content2)
    f2.close()
    
    folder = "./imggg/"
    content = await photo.read() # async & await로 동기 구현: 파일 불러오기가 끝나면 작동
    filename = photo.filename
    # 파일명 중복 대처
    type = filename[-4:] #.png
    filename = filename.replace(type, "")
    filename = filename + "_" + str(uuid4()) + type

    f = open(folder + filename, "wb")
    f.write(content)
    f.close()

def fileUpload(title: str=Form()):
    html = "<html><head><meta charset=\"utf-8\">"
    html += "</head><body>"
    html += "<h1>%s</h1>" %title
    html += "</body></html>"
    return HTMLResponse(html)

@app.get("/img.get")
def imgGet(fName:str):
    folder = "./imggg/"
    return FileResponse(folder + fName, filename = fName)

@app.get("/zip.get")
def zipGet(fName: str):
    folder = "./zipFolder/"
    return FileResponse(folder + fName, filename=fName)