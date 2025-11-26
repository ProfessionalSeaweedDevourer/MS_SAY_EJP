import fastapi
from fastapi.responses import HTMLResponse

app = fastapi.FastAPI()

@app.get("/convert")
def convert(num:float, what:str):
    if what == "len":
        result = num * 0.393701
        unit1 = "cm"
        unit2 = "inch"
    elif what == "size":
        result = num * 0.3025
        unit1 = "m^2"
        unit2 = "평"
    else:
        result = num * 1.8 + 32
        unit1 = "Celcius"
        unit2 = "Fahrenheit"

    html = "<html><head><meta charset=\"utf-8\">"
    html += "<link rel=\stylesheet\ href=\"nov19_FastAPI.css\">"
    html += "</head><body>"
    html += "<table>"
    html +="<tr><th>결과</th></tr>"
    html +="<tr><td align=\"center\">%.1f %s 를</td></tr>" % (num, unit1)
    html += "<tr><td align=\"center\">변환하면</td></tr>"
    html += "<tr><td align=\"center\">%.1f %s</td></tr>" % (result, unit2)
    html += "</table>"
    html += "</body></html>"
    return HTMLResponse(html)