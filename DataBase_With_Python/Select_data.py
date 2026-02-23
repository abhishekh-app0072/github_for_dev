# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password",
  database = "gfg",
  port=3306
)

# preparing a cursor object
cursorObject = dataBase.cursor()
 
query = "SELECT NAME, ROLL, AGE FROM STUDENT"
cursorObject.execute(query)
  
myresult = cursorObject.fetchall()
  
for x in myresult:
    print(x)

# disconnecting from server
dataBase.close()