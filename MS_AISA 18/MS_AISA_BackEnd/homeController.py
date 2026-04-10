from fastapi import FastAPI, Form, UploadFile

from sns.snsDAO import SNSDAO
from member.memberDAO import MemberDAO


app = FastAPI()
mDAO = MemberDAO()
sDAO = SNSDAO()


@app.get("/member.bye")
def memberBye(member, sDAO):
    return mDAO.bye(member, sDAO)


@app.get("/member.id.check")
def memberIdCheck(id):
    return mDAO.idCheck(id)


@app.get("/member.info.get")
def memberInfoGet(member):
    return mDAO.getMemberInfo(member)


@app.get("/member.info.psa.get")
def memberInfoPsaGet(file):
    return mDAO.getPsa(file)


@app.post("/member.info.update.no.psa")
async def memberInfoUpdateNoPsa(
    member: str = Form(),
    pw: str = Form(),
    name: str = Form(),
    addr1: str = Form(),
    addr2: str = Form(),
    addr3: str = Form(),
):
    return await mDAO.updateNoPsa(member, pw, name, addr1, addr2, addr3)


@app.post("/member.info.update")
async def memberInfoUpdate(
    psa: UploadFile,
    member: str = Form(),
    pw: str = Form(),
    name: str = Form(),
    addr1: str = Form(),
    addr2: str = Form(),
    addr3: str = Form(),
):
    return await mDAO.update(psa, member, pw, name, addr1, addr2, addr3)


@app.post("/sign.in")
def signIn(id: str = Form(), pw: str = Form()):
    return mDAO.signIn(id, pw)


@app.get("/sign.in.exp.refresh")
def signInExpRefresh(member):
    return mDAO.signInExpRefresh(member)


@app.post("/sign.up")
async def signUp(
    psa: UploadFile,
    id: str = Form(),
    pw: str = Form(),
    name: str = Form(),
    jumin1: str = Form(),
    jumin2: str = Form(),
    addr1: str = Form(),
    addr2: str = Form(),
    addr3: str = Form(),
):
    return await mDAO.signUp(psa, id, pw, name, jumin1, jumin2, addr1, addr2, addr3)


@app.get("/sns.post.delete")
def snsPostDelete(no):
    return sDAO.deletePost(no)


@app.get("/sns.post.get")
def snsPostGet(page: int, search):
    return sDAO.getPost(page, search)


@app.get("/sns.post.reply.delete")
def snsPostReplyDelete(no):
    return sDAO.deletePostReply(no)


@app.get("/sns.post.reply.write")
def snsPostReplyWrite(postno, member, txt):
    return sDAO.writePostReply(postno, member, txt)


@app.get("/sns.post.update")
def snsPostUpdate(no, txt):
    return sDAO.updatePost(no, txt)


@app.get("/sns.post.write")
def snsPostWrite(color, txt, member):
    return sDAO.writePost(color, txt, member)
