# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="127.0.0.1",
  user ="root",
  passwd ="password",
  database = "gfg",
  port=3306
)

# preparing a cursor object
cursorObject = dataBase.cursor()
 
query = "UPDATE STUDENT SET AGE = 23 WHERE Name ='Ram'"
cursorObject.execute(query)
dataBase.commit()

# disconnecting from server
dataBase.close()