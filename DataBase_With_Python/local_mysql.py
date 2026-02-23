import mysql.connector

dataBase = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password",
  port=3306
)

print("Connected Successfully")

dataBase.close()
