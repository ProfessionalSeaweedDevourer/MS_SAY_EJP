# 파일명 중복 문제 해결 라이브러리

class EJPFileNamer:
    @staticmethod
    async def upload(foler, file, pol):
        content = await file.read()
        filename = file.filename
        if pol == "uuid":
            filename = filename + "_" + str(uuid4())
        elif pol == "date":
            now = datetime.today()
            now = datetime.strftime(now, "%Y%m%d%H%M%S")
            filename = filename + "_" + now + type

        f = open(folder + filename, "wb")
        f.write(content)
        f.close()

        return filename