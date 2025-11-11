from datetime import datetime
from oracledb import connect

f = open("C:/OWMW.csv", "a", encoding = "utf-8")

con = connect("ericjpark/0000@195.168.9.249:1521/xe")

sql = "select * from OWMW"

cur = con.cursor()
cur.execute(sql)
for date, desc, temp, humi in cur:
    date = datetime.strftime(date, "%Y,%m,%d,%H,%M")
    date = "%s,%s,%.2f,%d\n" % (date, desc, temp, humi)
    f.write(data)

cur.close()
con.close()