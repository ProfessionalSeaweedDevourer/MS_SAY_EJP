from http.client import HTTPSConnection
from urllib.parse import quote

class NaverShoppingDAO:
    def getNSData(self,q):
        q=quote(q)

        h = {
            "X-Naver-Client-Id": "Jw3irlagRSw_EoSLFaC6",
            "X-Naver-Client-Secret": "zDIWqwbkyk"
            }

        huc = HTTPSConnection("openapi.naver.com")
        huc.request("GET", "/v1/search/shop.xml?query=" + q, headers=h)
        resBody = huc.getresponse().read()
        huc.close()
        return resBody