from datetime import timedelta, datetime, timezone
from fastapi.responses import JSONResponse
import jwt

class ProductDAO:

    def __init__(self):
        self.key = "1234"
        self.algorithm = "HS256"

    def reg(self, name, price):
        h = {"Access-Control-Allow-Origin": "*"}
        product = {
            "name": name,
            "price": price,
            "exp": datetime.now(timezone.utc) + timedelta(seconds=10),
        }
        token = jwt.encode(product, self.key, self.algorithm)
        return JSONResponse({"token": token}, headers=h)
    
    def get(self, token):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            payload = jwt.decode(token, self.key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            return JSONResponse({"error": "토큰이 만료되었습니다."}, status_code=401)
        except jwt.InvalidTokenError:
            return JSONResponse({"error": "유효하지 않은 토큰입니다."}, status_code=401)