import pandas as pd
import mysql.connector

# connect mysql
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3307",
    password="",
    database="stock_market_analysis"
)

cursor = connection.cursor()

# INSERT STOCK DATA

stock_df = pd.read_csv("cleaned_master_stock_data.csv")

stock_query = """INSERT INTO stock_data (ticker,date,open,high,low,close,volume,month)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

stock_data = [(row['ticker'],row['date'],row['open'],row['high'],row['low'],row['close'],row['volume'],row['month'])
              for index, row in stock_df.iterrows()]

# batch insertion
batch_size = 1000
for i in range(0, len(stock_data), batch_size):
    batch = stock_data[i:i + batch_size]
    cursor.executemany(stock_query, batch)
    connection.commit()
    print(f"{i + len(batch)} stock rows inserted...")

print("Stock Data Inserted Successfully")

# INSERT YEARLY RETURNS

returns_df = pd.read_csv("yearly_stock_returns_1.csv")

returns_query = """
INSERT INTO yearly_returns (ticker,first_close,last_close,yearly_return_percent)
VALUES (%s, %s, %s, %s)"""

returns_data = [(row['ticker'],row['first_close'],row['last_close'],row['yearly_return_percent'])
                for index, row in returns_df.iterrows()]

cursor.executemany(returns_query,returns_data)

connection.commit()

print("Yearly Returns Inserted Successfully")


# INSERT SECTOR PERFORMANCE

sector_df = pd.read_csv("sector_performance.csv")

sector_query = """INSERT INTO sector_performance (sector,yearly_return_percent)
VALUES (%s, %s)"""

sector_data = [(row['sector'],row['yearly_return_percent'])
    for index, row in sector_df.iterrows()]

cursor.executemany(sector_query,sector_data)

connection.commit()

print("Sector Performance Inserted Successfully")

# INSERT VOLATILITY DATA

volatility_df = pd.read_csv("stock_volatility.csv")

volatility_query = """INSERT INTO volatility_data (ticker,volatility)
VALUES (%s, %s)"""

volatility_data = [(row['ticker'],row['volatility'])
    for index, row in volatility_df.iterrows()]

cursor.executemany(volatility_query,volatility_data)

connection.commit()

print("Volatility Data Inserted Successfully")

cursor.close()
connection.close()

print("All Data Inserted Successfully")