import xml.etree.ElementTree as ET
from http.client import HTTPSConnection
import pandas as pd
import os
import datetime
import oracledb
from oracledb import connect
from json import loads

OWM_API_KEY = os.getenv("OWM_API_KEY", "")

hc = HTTPSConnection("api.openweathermap.org")
hc.request(
    "GET",
    f"/data/2.5/weather?q=seoul&appid={OWM_API_KEY}&units=metric&lang=kr",
)

# https://openweathermap.org/
# JSON(JavaScript Object Notation)

from http.client import HTTPSConnection
import json

hc = HTTPSConnection("api.openweathermap.org")
hc.request(
    "GET",
    f"/data/2.5/weather?q=seoul&appid={OWM_API_KEY}&units=metric&lang=kr",
)
res = hc.getresponse()
resBody = res.read()
txt = resBody.decode()
 
weatherData = json.loads(txt)
print(weatherData)
 
hc.close()

con = connect("ericjpark/0000@195.168.9.249:1521/xe")
weatherData = loads(resBody)
sql = "INSERT INTO OWMW "
sql += "VALUES(sysdate, '%s', %.2f, %d)" % (weatherData["weather"][0]["description"], weatherData["main"]["temp"], weatherData["main"]["humidity"])
 
cur = con.cursor()
cur.execute(sql)
con.commit()

cur.close()
con.close()