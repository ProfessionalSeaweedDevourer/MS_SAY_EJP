from unittest import result
from fastapi import FastAPI
from h11 import Response

from dec1_navershopDAO import NaverShoppingDAO

app = FastAPI()
nsDAO = NaverShoppingDAO

@app.get("/a.b") # 테스트용 (정상)
def ab():
    return {"A": "B"} 

@app.get("/naver.shopping.get")
def nsg(q:str):
    resultt = nsDAO.getNSData(q)
    h = {"Access-Control-Allow-Origin": "*"}
    return Response(resultt, media_type="application/xml", headers=h)