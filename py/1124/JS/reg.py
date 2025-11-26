# 입력값 유효성 검사를 위한 스크립트

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/product.reg")
def productReg(name: str, price: int):
    pass