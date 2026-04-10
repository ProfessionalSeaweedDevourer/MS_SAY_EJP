from datetime import datetime
from math import ceil
from fastapi.responses import JSONResponse
from http.client import HTTPSConnection
from json import loads
import jwt
from kwon.kwonDBManager import KwonDBManager


class SNSDAO:
    def __init__(self):
        self.jwtKey = "12341234"
        self.jwtAlgorithm = "HS256"
        self.postPerPage = 5
        self.setAllPostCount()

    def deletePost(self, no):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")
            sql = "delete from ms_aisa_sns_post "
            sql += "where masp_no = %s" % no
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allPostCount -= 1
                return JSONResponse({"result": "글 삭제 성공"}, headers=h)
            raise
        except:
            return JSONResponse({"result": "글 삭제 실패"}, headers=h)
        finally:
            KwonDBManager.closeConCur(con, cur)

    def deletePostReply(self, no):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")
            sql = "delete from ms_aisa_sns_post_reply "
            sql += "where maspr_no = %s" % no
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return JSONResponse({"result": "댓글 삭제 성공"}, headers=h)
            raise
        except:
            return JSONResponse({"result": "댓글 삭제 실패"}, headers=h)
        finally:
            KwonDBManager.closeConCur(con, cur)

    def getSearchPostCount(self, search):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")
            sql = "SELECT count(*) FROM ms_aisa_sns_post "
            sql += "WHERE masp_writer like '%s' or masp_txt like '%s'" % (
                search,
                search,
            )
            cur.execute(sql)

            for c in cur:
                return c[0]
        except:
            return 0
        finally:
            KwonDBManager.closeConCur(con, cur)

    def getPost(self, page, search):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")
            search = "%" + search + "%"
            postCount = self.allPostCount
            if search != "%%":
                postCount = self.getSearchPostCount(search)
            start = (page - 1) * self.postPerPage + 1
            end = page * self.postPerPage
            pageCount = ceil(postCount / self.postPerPage)
            sql = "SELECT * "
            sql += "FROM ( "
            sql += "    SELECT rownum AS rn, masp_no, masp_writer, masp_color, masp_txt, masp_date, mam_psa "
            sql += "    FROM ( "
            sql += "        SELECT masp_no, masp_writer, masp_color, masp_txt, masp_date, mam_psa "
            sql += "        FROM ms_aisa_sns_post, ms_aisa_member "
            sql += (
                "        WHERE masp_writer = mam_id and (masp_writer like '%s' or masp_txt like '%s') "
                % (search, search)
            )
            sql += "        ORDER BY masp_date desc "
            sql += "    ) "
            sql += ") "
            sql += "WHERE rn >= %d AND rn <= %d" % (start, end)
            cur.execute(sql)
            posts = []
            for _, no, writer, color, txt, date, psa in cur:
                posts.append(
                    {
                        "no": no,
                        "writer": writer,
                        "color": color,
                        "txt": txt,
                        "date": datetime.strftime(date, "%Y-%m-%d %H:%M:%S"),
                        "psa": psa,
                        "replys": self.getPostReply(no),
                    }
                )
            return JSONResponse({"pageCount": pageCount, "posts": posts}, headers=h)
        except Exception as e:
            print(e)
            return JSONResponse({"result": "조회 실패"}, headers=h)
        finally:
            KwonDBManager.closeConCur(con, cur)

    def getPostReply(self, postno):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")

            sql = "SELECT maspr_no, maspr_writer, maspr_txt, maspr_date "
            sql += "FROM ms_aisa_sns_post_reply "
            sql += "WHERE maspr_masp_no=%d" % postno
            sql += "ORDER BY maspr_date"
            cur.execute(sql)
            postReplys = []
            for no, writer, txt, date in cur:
                postReplys.append(
                    {
                        "no": no,
                        "postno": postno,
                        "writer": writer,
                        "txt": txt,
                        "date": datetime.strftime(date, "%Y-%m-%d %H:%M:%S"),
                    }
                )
            return postReplys
        except:
            return []
        finally:
            KwonDBManager.closeConCur(con, cur)

    def setAllPostCount(self):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")
            sql = "SELECT count(*) FROM ms_aisa_sns_post"
            cur.execute(sql)

            for c in cur:
                self.allPostCount = c[0]
        except:
            pass
        finally:
            KwonDBManager.closeConCur(con, cur)

    def updatePost(self, no, txt):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")
            txt = txt.replace('"', "").replace("\\n", "\r\n")
            sql = "update ms_aisa_sns_post "
            sql += "set masp_txt = '%s' " % txt
            sql += "where masp_no = %s" % no
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return JSONResponse({"result": "글 수정 성공"}, headers=h)
            raise
        except:
            return JSONResponse({"result": "글 수정 실패"}, headers=h)
        finally:
            KwonDBManager.closeConCur(con, cur)

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
                self.allPostCount += 1
                self.writeWeather(color)
                return JSONResponse({"result": "글쓰기 성공"}, headers=h)
            raise
        except:
            return JSONResponse({"result": "글쓰기 실패"}, headers=h)
        finally:
            KwonDBManager.closeConCur(con, cur)

    def writePostReply(self, postno, member, txt):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")
            member = jwt.decode(member, self.jwtKey, self.jwtAlgorithm)
            sql = "insert into ms_aisa_sns_post_reply "
            sql += (
                "values(ms_aisa_sns_post_reply_seq.nextval, %s, '%s', '%s', sysdate)"
                % (
                    postno,
                    member["id"],
                    txt,
                )
            )
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return JSONResponse({"result": "댓글쓰기 성공"}, headers=h)
            raise
        except:
            return JSONResponse({"result": "댓글쓰기 실패"}, headers=h)
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
