from datetime import datetime, timedelta, timezone
from os import remove
from fastapi.responses import FileResponse, JSONResponse
import jwt

from kwon.kwonDBManager import KwonDBManager
from kwon.kwonFileManager import KwonFileManager


class MemberDAO:
    def __init__(self):
        self.psaFolder = "./member/psa/"
        self.jwtKey = "12341234"
        self.jwtAlgorithm = "HS256"

    def bye(self, member, sDAO):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")
            member = jwt.decode(member, self.jwtKey, self.jwtAlgorithm)
            sql = "delete from ms_aisa_member where mam_id='%s'" % member["id"]
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                remove(self.psaFolder + member["psa"])
                sDAO.setAllPostCount()
                return JSONResponse({"result": "탈퇴 성공"}, headers=h)
            raise
        except:
            return JSONResponse({"result": "탈퇴 실패"}, headers=h)
        finally:
            KwonDBManager.closeConCur(con, cur)

    def idCheck(self, id):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")
            sql = "select count(*) from ms_aisa_member where mam_id='%s'" % id
            cur.execute(sql)
            for c in cur:
                if c[0] == 1:
                    return JSONResponse({"result": "중복"}, headers=h)
            return JSONResponse({"result": "사용가능"}, headers=h)
        except:
            return JSONResponse({"result": "DB문제"}, headers=h)
        finally:
            KwonDBManager.closeConCur(con, cur)

    def getMemberInfo(self, member):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            member = jwt.decode(member, self.jwtKey, self.jwtAlgorithm)
            member = {
                "id": member["id"],
                "pw": member["pw"],
                "name": member["name"],
                "birthday": member["birthday"],
                "address": member["address"],
                "psa": member["psa"],
            }
            return JSONResponse(
                {"result": "멤버 정보 존재", "member": member}, headers=h
            )
        except jwt.ExpiredSignatureError:
            return JSONResponse({"result": "만료"}, headers=h)
        except jwt.DecodeError:
            return JSONResponse({"result": "정보 없음"}, headers=h)

    def getPsa(self, file):
        return FileResponse(self.psaFolder + file, filename=file)

    def signIn(self, inputID, inputPW):
        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
            "Access-Control-Allow-Credentials": "true",
        }
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")

            sql = "SELECT * FROM ms_aisa_member WHERE mam_id='%s'" % inputID
            cur.execute(sql)
            count = 0
            for id, pw, name, birthday, address, psa in cur:
                count += 1
                if inputPW == pw:
                    member = {
                        "id": id,
                        "pw": pw,
                        "name": name,
                        "birthday": datetime.strftime(birthday, "%Y-%m-%d"),
                        "address": address,
                        "psa": psa,
                        "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
                    }
                    member = jwt.encode(member, self.jwtKey, self.jwtAlgorithm)
                    return JSONResponse(
                        {"result": "로그인 성공", "member": member}, headers=h
                    )
                else:
                    return JSONResponse({"result": "로그인 실패(PW)"}, headers=h)
            if count == 0:
                return JSONResponse({"result": "로그인 실패(미가입ID)"}, headers=h)
            raise
        except:
            return JSONResponse({"result": "로그인 실패(DB)"}, headers=h)
        finally:
            KwonDBManager.closeConCur(con, cur)

    def signInExpRefresh(self, member):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            member = jwt.decode(member, self.jwtKey, self.jwtAlgorithm)
            member = {
                "id": member["id"],
                "pw": member["pw"],
                "name": member["name"],
                "birthday": member["birthday"],
                "address": member["address"],
                "psa": member["psa"],
                "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
            }
            member = jwt.encode(member, self.jwtKey, self.jwtAlgorithm)
            return JSONResponse({"result": "갱신 완료", "member": member}, headers=h)
        except jwt.ExpiredSignatureError:
            return JSONResponse({"result": "만료"}, headers=h)
        except jwt.DecodeError:
            return JSONResponse({"result": "정보 없음"}, headers=h)

    async def signUp(self, psa, id, pw, name, jumin1, jumin2, addr1, addr2, addr3):
        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
            "Access-Control-Allow-Credentials": "true",
        }
        filename = await KwonFileManager.upload(self.psaFolder, psa, "uuid", 31457280)
        if filename == "fail":
            return JSONResponse({"result": "가입 실패(프사)"}, headers=h)

        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")

            if jumin2 == "1" or jumin2 == "2":
                birthday = "19" + jumin1
            else:
                birthday = "20" + jumin1

            addr = addr2 + "!" + addr3 + "!" + addr1

            sql = (
                "INSERT INTO ms_aisa_member values('%s', '%s', '%s', to_date('%s', 'YYYYMMDD'), '%s', '%s')"
                % (id, pw, name, birthday, addr, filename)
            )
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return JSONResponse({"result": "가입 성공"}, headers=h)
            raise
        except:
            remove(self.psaFolder + filename)
            return JSONResponse({"result": "가입 실패"}, headers=h)
        finally:
            KwonDBManager.closeConCur(con, cur)

    async def update(self, psa, member, pw, name, addr1, addr2, addr3):
        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
            "Access-Control-Allow-Credentials": "true",
        }
        filename = await KwonFileManager.upload(self.psaFolder, psa, "uuid", 31457280)
        if filename == "fail":
            return JSONResponse({"result": "수정 실패(프사)"}, headers=h)
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")
            member = jwt.decode(member, self.jwtKey, self.jwtAlgorithm)
            addr = addr2 + "!" + addr3 + "!" + addr1
            sql = "update ms_aisa_member "
            sql += "set mam_pw='%s', mam_name='%s', mam_address='%s', mam_psa='%s' " % (
                pw,
                name,
                addr,
                filename,
            )
            sql += "where mam_id='%s'" % member["id"]
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                remove(self.psaFolder + member["psa"])
                newMember = {
                    "id": member["id"],
                    "pw": pw,
                    "name": name,
                    "birthday": member["birthday"],
                    "address": addr,
                    "psa": filename,
                    "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
                }
                newMember = jwt.encode(newMember, self.jwtKey, self.jwtAlgorithm)
                return JSONResponse(
                    {"result": "수정 성공", "member": newMember}, headers=h
                )
            raise
        except:
            remove(self.psaFolder + filename)
            return JSONResponse({"result": "수정 실패"}, headers=h)
        finally:
            KwonDBManager.closeConCur(con, cur)

    async def updateNoPsa(self, member, pw, name, addr1, addr2, addr3):
        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
            "Access-Control-Allow-Credentials": "true",
        }
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.251:1521/xe")
            member = jwt.decode(member, self.jwtKey, self.jwtAlgorithm)
            addr = addr2 + "!" + addr3 + "!" + addr1
            sql = "update ms_aisa_member "
            sql += "set mam_pw='%s', mam_name='%s', mam_address='%s' " % (
                pw,
                name,
                addr,
            )
            sql += "where mam_id='%s'" % member["id"]
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                newMember = {
                    "id": member["id"],
                    "pw": pw,
                    "name": name,
                    "birthday": member["birthday"],
                    "address": addr,
                    "psa": member["psa"],
                    "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
                }
                newMember = jwt.encode(newMember, self.jwtKey, self.jwtAlgorithm)
                return JSONResponse(
                    {"result": "수정 성공", "member": newMember}, headers=h
                )
            raise
        except Exception as e:
            print(e)
            return JSONResponse({"result": "수정 실패"}, headers=h)
        finally:
            KwonDBManager.closeConCur(con, cur)
