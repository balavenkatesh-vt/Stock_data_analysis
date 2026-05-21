import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="",
    database="stock_market_analysis"
)
cursor = connection.cursor()

#creating stock_data
cursor.execute("""CREATE TABLE IF NOT EXISTS stock_data (id INT AUTO_INCREMENT PRIMARY KEY,ticker VARCHAR(50),
date DATETIME,open FLOAT,high FLOAT,low FLOAT,close FLOAT,volume BIGINT,month VARCHAR(20))""")

print("stock_data table created successfully")

# yearly_returns table
cursor.execute("""CREATE TABLE IF NOT EXISTS yearly_returns (id INT AUTO_INCREMENT PRIMARY KEY,ticker VARCHAR(50),
first_close FLOAT,last_close FLOAT,yearly_return_percent FLOAT)""")

print("yearly_returns table created successfully")

# sector_performance table
cursor.execute("""CREATE TABLE IF NOT EXISTS sector_performance (id INT AUTO_INCREMENT PRIMARY KEY,sector VARCHAR(100),
yearly_return_percent FLOAT)""")

print("sector_performance table created successfully")

# volatility_data table
cursor.execute("""CREATE TABLE IF NOT EXISTS volatility_data (id INT AUTO_INCREMENT PRIMARY KEY,
ticker VARCHAR(50),volatility FLOAT)""")

print("volatility_data table created successfully")

cursor.close()
connection.close()
