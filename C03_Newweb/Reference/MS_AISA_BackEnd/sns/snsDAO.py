from fastapi.responses import JSONResponse
from http.client import HTTPSConnection
from json import loads
import jwt
from kwon.kwonDBManager import KwonDBManager


class SNSDAO:
    def __init__(self):
        self.jwtKey = "12341234"
        self.jwtAlgorithm = "HS256"

    def writePost(self, color, txt, member):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")
            member = jwt.decode(member, self.jwtKey, self.jwtAlgorithm)
            txt = txt.replace('"', "").replace("\\n", "\r\n")
            sql = "insert into ms_aisa_sns_post "
            sql += "values(ms_aisa_sns_post_seq.nextval, '%s', '%s', '%s', sysdate)" % (
                member["id"],
                color,
                txt,
            )
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.writeWeather(color)
                return JSONResponse({"result": "글쓰기 성공"}, headers=h)
            raise
        except:
            return JSONResponse({"result": "글쓰기 실패"}, headers=h)
        finally:
            KwonDBManager.closeConCur(con, cur)

    def writeWeather(self, color):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")
            hc = HTTPSConnection("api.openweathermap.org")
            hc.request(
                "GET",
                "/data/2.5/weather?q=seoul&appid=***REMOVED_OWM_KEY***&units=metric&lang=kr",
            )
            resBody = hc.getresponse().read()
            hc.close()
            weatherData = loads(resBody)
            sql = "insert into ms_aisa_weather_color "
            sql += "values('%s', %.3f, %d, '%s')" % (
                weatherData["weather"][0]["description"],
                weatherData["main"]["temp"],
                weatherData["main"]["humidity"],
                color,
            )
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
            raise
        except:
            pass
        finally:
            KwonDBManager.closeConCur(con, cur)
