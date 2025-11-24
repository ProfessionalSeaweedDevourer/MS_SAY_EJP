from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/xycalc")
def xyCalc(x:int, y:int):
    z = x+ y
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<h1>%d</h1>" %z
    html += "</body></html>"
    return HTMLResponse(html)

@app.post("/gugudan.show")
def fs(start:int=Form(), end:int=Form()):
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    for dan in range(start, end+1):
        html += "<table border=\"1\" style=\"float:left;\">"
        html += "<tr><th>%단</th></tr>" %dan
        for i in range(1,10):
            html += "<tr><td>%d x %d = %d</td></tr>" % (dan, i, dan*i)
        html += "</table>"
    html += "</body></html>"
    return HTMLResponse(html)