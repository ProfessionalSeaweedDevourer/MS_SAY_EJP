from fastapi import FastAPI

app = FastAPI()

@app.get("/html.test")
def htmlTest():
    html = ""
    pass
