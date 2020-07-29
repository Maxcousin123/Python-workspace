import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='maxcousin',
    password='secret :)',
    database='testdb' #to request a specific database
    )
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE rovan (code INTEGER(10), size VARCHAR(255), price integer(10), color VARCHAR(255))")