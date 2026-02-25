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
 
query ="Drop Table if exists EMP;"

cursorObject.execute(query)
dataBase.commit()

# disconnecting from server
dataBase.close()