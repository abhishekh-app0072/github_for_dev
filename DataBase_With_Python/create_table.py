# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="127.0.0.1",
  user ="root",
  passwd ="password",
  port=3306,
  database = "gfg"
)

# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating table 
studentRecord = """CREATE TABLE Student (
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5),
                   AGE INT
                   )"""
 
# table created
cursorObject.execute(studentRecord) 
 
# disconnecting from server
dataBase.close()