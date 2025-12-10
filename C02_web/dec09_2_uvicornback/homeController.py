from fastapi import FastAPI

app = FastAPI()

@app.get("/a.b")
def ab():
    return {"A": "B"}