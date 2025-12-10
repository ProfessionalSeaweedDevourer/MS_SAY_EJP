from http.client import HTTPConnection
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import fromstring
from oracledb import connect

hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET", "/***REMOVED_SEOUL_KEY***/xml/RealtimeCityAir/1/25/")
res = hc.getresponse()
resBody = res.read()
hc.close()

con = connect("ericjpark/0000@195.168.9.249:1521/xe")
cur = con.cursor()

seoulDustDataa = fromstring(resBody)
rowsss = seoulDustDataa.iter("row")
for r in rowsss:
    msrrgn_nm = r.find("SAREA_NM").text
    msrste_nm = r.find("MSRSTN_NM").text
    pm10 = r.find("PM").text
    pm25 = r.find("FPM").text
    idex_nm = r.find("CAI_GRD").text

    sql = "insert into seoul_dust "
    sql += "values(sysdate, '%s', '%s', '%s', '%s', '%s')" % (msrrgn_nm, msrste_nm, pm10, pm25, idex_nm)

    cur = con.cursor() # 커서는 1회용.
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()