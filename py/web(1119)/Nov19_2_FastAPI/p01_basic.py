# 둘 문법이 거의 같음
# Flask : 자체 WAS기능 포함 -> 단독실행가능
#       응답형태를 딱히 가리지 않음
# FastAPI : 자체 WAS기능 포함 -> 단독실행가능한데
#       주로 따로 WAS 필요 -> uvicorn에서 실행하는 형태로
#       기본적으로 JSON으로 응답

# 시작 - cmd
#   pip install fastapi
#   pip install uvicorn[standard]

# Windows에서 이 파일 있는 곳으로 가서 cmd
#   uvicorn 파일명(확장자말고):app --host=0.0.0.0 --port=???? --reload
#   uvicorn p01_basic:app --host=0.0.0.0 --port=7777 --reload
from fastapi import FastAPI

app = FastAPI()

@app.get("/te.st")
def test():
    snack = {"name": "초코파이", "price": 5000}
    return snack
