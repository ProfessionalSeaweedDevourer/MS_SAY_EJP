import pandas as pd
from oracledb import connect
 
con = connect("leewoo/3214@195.168.9.198:1521/xe")
# sql = "select * from seoul_dust"
# sql = "select avg(sd_pm10 + sd_pm25), min(sd_pm10 + sd_pm25) "
# sql += "from seoul_dust"
sql = "select sd_msrste_nm "
sql += "from seoul_dust "
sql += "where sd_pm10 + sd_pm25 = ("
sql += "    select max(sd_pm10 + sd_pm25) "
sql += "    from seoul_dust"
sql += ") "
df = pd.read_sql(sql, con)
con.close()
print(df)
 
# df["SD_PM_SUM"] = df["SD_PM10"] + df["SD_PM25"] # 미세+초미세 구해서
# print(df["SD_PM_SUM"].mean()) # 평균
# print(df["SD_PM_SUM"].min()) # 최소값
# print(df[df["SD_PM_SUM"] == df["SD_PM_SUM"].max()]["SD_MSRSTE_NM"]) # 가장 심했던 구 이름