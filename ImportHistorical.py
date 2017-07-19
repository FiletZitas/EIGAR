#EIGAR Equity Information gathering robot
from yahoo_finance import Share
import mysql.connector

YTicker = 'IS3N.DE'
SDate = '2016-01-01'
EDate = '2017-04-28'

config = {
'user': 'USER',
'password': 'PASSWORD',
'host': '192.168.XXX.XXX',
'port': '3306',
'database': 'DBNAME',
'raise_on_warnings': True,}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
yahoo = Share(YTicker)
DBName = YTicker.replace(".", "_")
cursor.execute("""CREATE TABLE IF NOT EXISTS """ + DBName + """(
    Symbol VARCHAR(255),
    Date DATE,
    Adj_Close FLOAT,
    High FLOAT,
    Low FLOAT,
    Volume FLOAT)
    COMMENT=""" + '"' + yahoo.get_name() + '"' + """;""")
cnx.commit()
add_value = ("INSERT INTO " + DBName  + " (Symbol, Date, Adj_Close, High, Low, Volume) VALUES (%s, %s, %s, %s, %s, %s)")
L = yahoo.get_historical(SDate, EDate)
for items in L:
    data = (items['Symbol'],items['Date'],items['Adj_Close'],items['High'],items['Low'],items['Volume'])
    print(data)
    cursor.execute(add_value, data)
    cnx.commit()