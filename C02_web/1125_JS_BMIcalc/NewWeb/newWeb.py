from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/xml.test")
def xmlTest():
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += "<snacks>"
    
    # 첫 번째 상품 (하나의 유효한 <snack> 요소)
    xml += "<snack>"
    xml +="<s_name>초코파이</s_name>" # 클라이언트 스크립트에 맞게 태그 이름 변경
    xml +="<s_price>5000</s_price>" # 클라이언트 스크립트에 맞게 태그 이름 변경
    xml += "</snack>"
    
    # 두 번째 상품 (두 번째 유효한 <snack> 요소)
    xml += "<snack>"
    xml +="<s_name>새우깡</s_name>" # 클라이언트 스크립트에 맞게 태그 이름 변경
    xml +="<s_price>3000</s_price>" # 클라이언트 스크립트에 맞게 태그 이름 변경
    xml += "</snack>"
    
    xml += "</snacks>"
    
    h = {"Access-Control-Allow-Origin" : "*"}
    return Response(xml, media_type="application/xml", headers=h)

@app.get("/json.test")
def jsonTest():
    json = [
        {"s_name":"초코파이", "s_price":5000},
        {"s_name":"새우깡", "s_price":3000}
    ]
    return json

# XML / JSON을 외부에서도 쓸 수 있게 하기
# > Access-Control-Allow-Origin: 응답 헤더
