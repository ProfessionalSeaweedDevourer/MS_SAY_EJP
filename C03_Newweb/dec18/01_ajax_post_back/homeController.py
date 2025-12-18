from fastapi import FastAPI
from calculator import Calculator

app = FastAPI()
c = Calculator()

@app.get("/calc.do")
def calculateDo(x:int, y:int):
    return c.calculate(x, y)