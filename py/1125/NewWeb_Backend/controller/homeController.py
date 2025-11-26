from fastapi import FastAPI
import oracledb
from lib.ejpDBManager import ejpDBManager

app = FastAPI()

# .../snack.reg?n=빼빼로&p=1500

# 데이터 등록 
@app.get("/cnfood.reg")
def cnfoodReg(n: str, p: int):
    print(n, p)

# 데이터 조회
@app.get("/cnfood.get")
def cnfoodGet():
    pass