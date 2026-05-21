import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port = "3307",
    user="root",
    password=""
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS stock_market_analysis")

print("Database Created Successfully")
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)
cursor.close()
connection.close()