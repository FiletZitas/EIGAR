#EIGAR Equity Information gathering robot
from yahoo_finance import Share
import mysql.connector
import time

config = {
'user': 'USERNAME',
'password': 'PASSWORD',
'host': '192.168.XXX.XXX',
'port': '3306',
'database': 'dbname',
'raise_on_warnings': True,}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
for YTicker in tables:
    x = str(YTicker[0])
    Symbol = x.replace("_", ".")
    print (Symbol)
    yahoo = Share(Symbol)
    Date = time.strftime("%Y-%m-%d")
    Adj_Close = yahoo.get_price()
    High = yahoo.get_days_high()
    Low = yahoo.get_days_low()
    Volume = yahoo.get_volume()
    add_value = ("INSERT INTO " + YTicker[0] + " (Symbol, Date, Adj_Close, High, Low, Volume) VALUES (%s, %s, %s, %s, %s, %s)")
    data = (Symbol, Date, Adj_Close, High, Low, Volume)
    cursor.execute(add_value, data)
    cnx.commit()
    print (YTicker[0] + " updated... to" + Adj_Close)




