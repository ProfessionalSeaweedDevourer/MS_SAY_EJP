from flask import Flask

app = Flask(__name__)

# http://195.168.9.153:8888/html.test
@app.get("/html.test")
def htmlTest():
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<marquee>ㅋㅋ</marquee>"
    html += "</body></html>"
    return html

# http://195.168.9.153:8888/xy.calculate
@app.get("/xy.calculate")
def xyCalculate():
    a = 10
    b = 20
    c = a + b
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<h1>%d</h1>" % c
    html += "</body></html>"
    return html

# http://195.168.9.153:8888/gugudan.show
@app.get("/gugudan.show")
def gs():
    html = "<html><head><meta charset=\"utf-8\"></head><body>"

    for dan in range(2, 10):
        html += "<table border=\"1\" style=\"float:left;\">"
        html += "<tr><th>%d단</th></tr>" % dan
        for i in range(1, 10):
            html += "<tr><td>%d x %d = %d</td></tr>" % (dan, i, dan * i)
        html += "</table>"

    html += "</body></html>"
    return html

if __name__ == "__main__":
    app.run("0.0.0.0", 8888, True)