# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
   host="127.0.0.1",
  user="root",
  password="password",
  port=3306
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
cursorObject.execute("CREATE DATABASE gfg")