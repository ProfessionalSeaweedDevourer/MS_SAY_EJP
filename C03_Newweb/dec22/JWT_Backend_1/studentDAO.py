# JWT: JSON Web Token. JSON으로 이루어진 암호화 + 시간 제한 도입
from fastapi.responses import JSONResponse
import jwt
from datetime import timedelta, timezone, datetime

class StudentDAO:

    def __init__(self):
        self.jwtKey = "test"
        self.jwtAlgorithm = "HS256"

    def reg(self, name, age):
        h = {"Access-Control-Allow-Origin": "*"}
        # exp: expire 시간으로 쓸 데이터.
        result = {
            "name": name,
            "age": age,
            "exp": datetime.now(timezone.utc) + timedelta(seconds=10),
        }

        # datetime.today() vs datetime.now(): 차이 없음
        # datetime.now(datetime.utc): 표준 시간대
        # => 표준 시간대에서 10초 지난 시간: datetime.now(datetime.utc) + timedelta(seconds=10)

        # 암호화된 jwt 결과물을 하나의 string으로 저장: "대상, 키, 사용 알고리즘"
        jwtResult = jwt.encode(result, "test", "HS256")

        # string 꼴의 jwt를 JSON으로 풀어 주기
        jwtResult2 = {"EJPJWT": jwtResult}
        return JSONResponse(jwtResult2, headers=h)

    def get(self, encodedJWT):
        h = {"Access-Control-Allow-Origin": "*"}
        # 복호화
        try:
            result = jwt.decode(encodedJWT, self.jwtKey, self.jwtAlgorithm)
            result = {
                "result": "복호화 결과",
                "name": result["name"],
                "age": result["age"],
            }
        except jwt.ExpiredSignatureError:
            result = {"result": "시간초과"}
        except jwt.DecodeError:
            result = {"result": "JWT 없음"}
        return JSONResponse(result, headers=h)
