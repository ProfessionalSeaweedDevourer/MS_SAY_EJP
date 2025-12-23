from fastapi import FastAPI
from productDAO import ProductDAO
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # 모든 도메인 허용 (테스트용)
    allow_credentials=True,
    allow_methods=["*"],           # GET, POST 등 모든 메소드 허용
    allow_headers=["*"],           # 모든 헤더 허용
)

pDAO = ProductDAO()

@app.get("/product.reg")
def productReg(name:str, price:int):
    return pDAO.reg(name, price)

@app.get("/product.get")
def productGet(token: str = None): # 기본값을 지정하거나 타입을 명시
    if token is None or token == "null":
        return {"error": "토큰이 없습니다."}
    return pDAO.get(token)