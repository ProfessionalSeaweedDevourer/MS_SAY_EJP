from fastapi import FastAPI

app = FastAPI()

@app.get("/te.st")
def test():
    snack = {"name": "초코파이", "price": 5000}
    return snack
