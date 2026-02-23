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
 
sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
VALUES (%s, %s, %s, %s, %s)"
val = ("Ram", "CSE", "85", "B", "19")
  
cursorObject.execute(sql, val)
dataBase.commit()
  
# disconnecting from server
dataBase.close()