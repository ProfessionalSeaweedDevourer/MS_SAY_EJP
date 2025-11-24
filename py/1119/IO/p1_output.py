from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/signup")
def signup(id:str):
    html = "<html><head><meta charset=\"utf-8\"></head></body>"
    html += "<h1>%s</h1>" % id
    html += "</body></html>"
    return HTMLResponse