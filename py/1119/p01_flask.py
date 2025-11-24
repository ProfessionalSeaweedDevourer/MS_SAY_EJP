from flask import Flask, request

app = Flask(__name__)

@app.get("/te.st") # 이 주소로 클라이언트로부터 GET 요청이 오면
def test(): # 이 함수가 실행됨
    print("Flask") # 클라이언트로 응답할 문자열

# request parameters: 클라이언트가 WAS로 보내는 요청.

#주소 체계: 프로토콜://호스트:포트/경로?쿼리스트링

# HTTP 요청 메서드: GET, POST, PUT, DELETE ...
# GET: 주소창에 쿼리스트링을 붙여서 요청
# POST: 폼 데이터를 본문에 담아서 요청
@app.get("/xycalc")
def xycalc():
    # 1. request.args를 사용하여 쿼리 매개변수 'x'와 'y'를 가져옵니다.
    # get('name', default_value)를 사용하여 값이 없을 때 오류를 방지합니다.
    x_str = request.args.get('x', '0')
    y_str = request.args.get('y', '0')
    
    # 2. 문자열로 들어온 값을 정수로 변환합니다.
    try:
        x = int(x_str)
        y = int(y_str)
        sum_value = x + y
        
        # 3. 계산 결과를 HTML로 구성하여 반환합니다.
        html = "<html><head><meta charset='utf-8'></head><body>"
        html += "<h1>x + y 계산 결과</h1>"
        html += f"<p>입력된 x 값: **{x}**</p>"
        html += f"<p>입력된 y 값: **{y}**</p>"
        html += f"<p>**x + y = {sum_value}**</p>"
        html += "</body></html>"
        
    except ValueError:
        # 숫자가 아닌 값이 입력되었을 때의 오류 처리
        html = "<html><body><h1>오류</h1><p>유효한 숫자(x, y)를 입력해 주십시오.</p></body></html>"

    return html # HTML 응답 반환

@app.get("/gugudan.show")
def gugudan():
    # 1. GET 요청이므로 request.args를 사용하여 쿼리 매개변수를 가져옵니다.
    start_str = request.args.get("start")
    end_str = request.args.get("end")
    
    html = "<html><head><meta charset='utf-8'></head><body>"
    html += "<h1>구구단 출력</h1>"
    
    # 2. 유효성 검사 및 정수 변환을 수행합니다.
    if not start_str or not end_str:
        html += "<p>시작 단(start)과 끝 단(end) 값을 모두 입력해 주십시오.</p>"
        html += "</body></html>"
        return html
        
    try:
        s = int(start_str)
        e = int(end_str)
        
        # 3. 구구단 로직을 실행합니다. (끝 값 e를 포함하기 위해 e + 1을 사용)
        # 2단부터 9단까지만 출력하도록 범위를 제한할 수도 있지만, 요청에 따라 사용자가 지정한 범위 s부터 e까지 처리합니다.
        
        # 시작 단이 끝 단보다 크면 오류 메시지 출력
        if s > e:
            html += "<p>시작 단이 끝 단보다 클 수 없습니다. 값을 확인해 주십시오.</p>"
        else:
            for dan in range(s, e + 1): # 끝 단(e)을 포함하기 위해 +1
                html += "<table border=\"1\" style='display:inline-block; margin-right: 20px;'>"
                # <th> 태그 닫는 괄호 '>'와 <tr> 닫는 괄호 '>' 수정
                html += "<tr><th style='background-color: #f0f0f0;'>%d단</th></tr>" % dan
                for su in range(1, 10):
                    html += "<tr><td>%d x %d = %d</td></tr>" % (dan, su, dan * su)
                html += "</table>"

    except ValueError:
        # 숫자가 아닌 값이 입력되었을 때의 오류 처리
        html += "<p>시작 단과 끝 단은 반드시 유효한 정수여야 합니다. 값을 확인해 주십시오.</p>"

    html += "</body></html>"
    return html

if __name__ == "__main__": 
    app.run("0.0.0.0", 9999, True) # 접속 허용 주소, 포트, 디버그 모드 설정
