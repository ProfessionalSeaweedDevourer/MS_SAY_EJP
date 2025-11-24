# HTML : 웹사이트
# -----------디자인 부족
# HTML : 웹사이트 뼈대 : 디자인 언어
# CSS : HTML 디자인 서포트 : 디자인 언어
# -----------프로그래밍언어쪽 기능 부족
# 클라이언트가 웹사이트 요청하면
# HTML + CSS를 만들어서 응답하는
# Python프로그램

# Web Server
#   HTML/CSS를 올려놓으면
#   클라이언트가 요청했을때 HTML/CSS를 응답해주는 서버
# WAS(Web Application Server)
#   Web Server + 프로그램 실행되는

# Flask : Python WAS 라이브러리
# 시작 - cmd
#   pip install flask

# HTTP통신
#   클라이언트가 서버에 요청하면
#   서버는 그 요청에 대해 응답

from flask import Flask

app = Flask(__name__)

@app.get("/te.st") # /te.st라는 주소로 클라이언트로부터 GET방식 요청받으면
def test(): # 이 함수 자동 실행
    return "abcd" # abcd라고 응답

if __name__ == "__main__":
    # 접속허용주소, 포트번호, 디버그모드(로그출력, 자동재시작)여부
    app.run("0.0.0.0", 9999, True)