from http.client import HTTPConnection
from json import loads
import pandas as pd
 
hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET", "/***REMOVED_SEOUL_KEY***/json/RealtimeCityAir/1/25/")
res = hc.getresponse()
resBody = res.read()
hc.close()
 
dustData = loads(resBody)
dustDF = pd.DataFrame(dustData["RealtimeCityAir"]["row"])
print(dustDF)
print("-----")
dustDF["PM_SUM"] = dustDF["PM"] + dustDF["FPM"]
dustDF["PM_AVG"] = dustDF["PM_SUM"] / 2
print(dustDF[["MSRSTN_NM", "PM_AVG"]])

# db선에서 해결할 수 있는 문제기는 하지만...