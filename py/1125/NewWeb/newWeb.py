from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/xml.test")
def xmlTest():
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += "<snacks>"
    xml +="<snack>"
    xml +="<name>초코파이</name>"
    xml +="<price>5000</price>"
    xml +="<name>새우깡</name>"
    xml +="<price>3000</price>"
    xml +="</snack>"
    xml +="</snacks>"
    return Response(xml, media_type="application/xml")

@app.get("/json.test")
def jsonTest():
    json = [
        {"s_name":"초코파이", "s_price":5000},
        {"s_name":"새우깡", "s_price":3000}
    ]
    return json

# XML / JSON을 외부에서도 쓸 수 있게 하기
# > Access-Control-Allow-Origin: 응답 헤더
