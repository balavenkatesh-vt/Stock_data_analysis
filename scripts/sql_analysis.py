import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3307",
    password="",
    database="stock_market_analysis"
)

cursor = connection.cursor()

# TOP 10 GAINERS

query = """SELECT ticker,yearly_return_percent FROM yearly_returns 
ORDER BY yearly_return_percent 
DESC LIMIT 10"""

cursor.execute(query)
result = cursor.fetchall()

# converting this to dataframe for better output format like tabled structure:
top_gainers_df = pd.DataFrame(result,columns=['ticker','yearly_return_percent'])

print("TOP 10 GAINERS")
print(top_gainers_df)

# TOP 10 LOSERS

query = """SELECT ticker, yearly_return_percent
FROM yearly_returns
ORDER BY yearly_return_percent ASC
LIMIT 10"""

cursor.execute(query)
result = cursor.fetchall()

top_losers_df = pd.DataFrame(result,columns=['ticker','yearly_return_percent'])

print("TOP 10 LOSERS")
print(top_losers_df)

# AVERAGE CLOSE PRICE

query = """SELECT AVG(close) AS average_close_price
FROM stock_data"""

cursor.execute(query)
result = cursor.fetchall()

avg_close_df = pd.DataFrame(result,columns=['average_close_price'])

print("AVERAGE CLOSE PRICE")
print(avg_close_df)

# AVERAGE VOLUME

query = """SELECT AVG(volume) AS average_volume
FROM stock_data"""

cursor.execute(query)
result = cursor.fetchall()

avg_volume_df = pd.DataFrame(result,columns=['average_volume'])

print("AVERAGE VOLUME")
print(avg_volume_df)

# TOP 10 MOST VOLATILE STOCKS

query = """SELECT ticker,volatility
FROM volatility_data
ORDER BY volatility DESC
LIMIT 10"""

cursor.execute(query)
result = cursor.fetchall()

volatile_df = pd.DataFrame(result,columns=['ticker','volatility'])

print("TOP 10 MOST VOLATILE STOCKS")
print(volatile_df)

# BEST PERFORMING SECTORS

query = """SELECT sector,yearly_return_percent
FROM sector_performance
ORDER BY yearly_return_percent DESC"""

cursor.execute(query)
result = cursor.fetchall()

sector_df = pd.DataFrame(result,columns=['sector','yearly_return_percent'])

print("BEST PERFORMING SECTORS")
print(sector_df)