from flask import Flask, request

app = Flask(__name__)

# request parameter : 클라이언트가 WAS로 보내는 정보

# 인터넷 주소 체계
#   프로토콜://서버IP주소:포트/지정한주소?변수명=값&변수명=값&...

# HTTP통신 요청
#   GET방식
#       주소 직접 쳐서 접속, <a> -> 일반적
#       reqParam이 주소에
#   POST방식
#       form/프로그램을 통해서만 가능 -> 특수
#       reqParam이 내부적으로 전달 -> 보안성 높음

# http://195.168.9.153:8888/xy.calculate?xxx=10&yyy=20
@app.get("/xy.calculate")
def xyCalculate():
    # request.args.get("reqParam변수명") -> str
    x = int(request.args.get("xxx"))
    y = int(request.args.get("yyy"))
    z = x + y
    html = "<html><head><meta charset=\"utf-8\"></head><body>"
    html += "<h1>%d</h1>" % z
    html += "</body></html>"
    return html

# http://195.168.9.153:8888/gugudan.show
@app.post("/gugudan.show")
def gs():
    #s = int(request.args.get("start"))
    #e = int(request.args.get("end"))
    s = int(request.form["start"])
    e = int(request.form["end"]) # request.form["reqParam변수명"]

    html = "<html><head><meta charset=\"utf-8\"></head><body>"

    for dan in range(s, e+1):
        html += "<table border=\"1\" style=\"float:left;\">"
        html += "<tr><th>%d단</th></tr>" % dan
        for i in range(1, 10):
            html += "<tr><td>%d x %d = %d</td></tr>" % (dan, i, dan * i)
        html += "</table>"

    html += "</body></html>"
    return html

if __name__ == "__main__":
    app.run("0.0.0.0", 8888, True)