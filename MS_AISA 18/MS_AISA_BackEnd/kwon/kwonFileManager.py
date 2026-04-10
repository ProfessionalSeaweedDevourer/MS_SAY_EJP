from datetime import datetime
from uuid import uuid4


class KwonFileManager:
    
    @staticmethod
    async def upload(folder, file, mode, maxSize):
        try:
            content = await file.read()
            if len(content) > maxSize:
                return "fail"
            filename = file.filename
            type = filename[-4:]
            filename = filename.replace(type, "")

            if mode == "uuid":
                filename = filename + "_" + str(uuid4()) + type
            elif mode == "date":
                now = datetime.today()
                now = datetime.strftime(now, "%Y%m%d%H%M%S")
                filename = filename + "_" + now + type
            
            f = open(folder + filename, "wb")
            f.write(content)
            f.close()

            return filename
        except:
            return "fail"