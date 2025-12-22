from fastapi import FastAPI
import studentDAO as sDAO


app = FastAPI()

def studentReg(name: str, age:int):
    return sDAO.reg(name, age)

@app.get("/student.get")
def studentGet(jwt:str):
    return sDAO.get(jwt)