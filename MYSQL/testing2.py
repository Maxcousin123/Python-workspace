import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='maxcousin',
    password='www.moh.com',
    database='testdb' #to request a specific database
    )




mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM rovan')# * = all
myresult = mycursor.fetchall()
for row in myresult:
    print(row)