from fastapi.responses import JSONResponse

class Calculator:
    def calculate(self, x, y):
        result = {
            "sum": x+y, "sub": x-y, "mult": x*y, "div": x/y
        }
        h = {"Access-Control-Allow-Origin": "*"}
        return JSONResponse(result, headers=h)