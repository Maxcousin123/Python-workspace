import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='maxcousin',
    password='secret :)',
    database='testdb' #to request a specific database
    )
mycursor = mydb.cursor()




mycursor.execute("CREATE DATABASE ....")
#to create a database

mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
#to show databases

mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
#to create tables

mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)
#to show tables

sqlFormula="INSERT INTO 'Table name' (name, age) VALUES (%s, %s)"
student1 = ("Rachel", 22)
mycursor.execute(sqlFormula, student1)
mydb.commit()
#to give values

sqlFormula = "INSERT INTO 'Table name' (name, age) VALUES (%s, %s)"
student1 = [("Rachel", 22),
           ("Rachel", 22),
           ("Rachel", 22),
           ("Rachel", 22),]
mycursor.executemany(sqlFormula, student1)
mydb.commit()
#to give multiple values

mycursor.execute('SELECT * FROM "Table name"')# * = all

myresult = mycursor.fetchall()
for row in myresult:
    print(row)
#to get all data

mycursor.execute('SELECT * FROM "Table name"')# * = all
myresult = mycursor.fetchone()
for row in myresult:
    print(row)
#to get ONE data

sql = "SELECT * FROM 'table name' WHERE age = 13"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)
#to get specific data

sql = "SELECT * FROM 'table name' WHERE name LIKE @@%"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)
#to get data that has part written between %-% or before it

sql = "SELECT * FROM 'table name' WHERE name LIKE @@%"
mycursor.execute(sql,('name',))
myresult = mycursor.fetchall()
for result in myresult:
    print(result)
#to get a specific data

sql = "UPDATe table name SET age = 13 WHERE name = '...' "
mycursor.execute(sql)
mydb.commit()
#to edit data

sql = "SELECT * FROM 'table name' LIMIT 'int'"
myresult = mycursor.fetchall()
for result in myresult:
    print(result)
#to get data all the way to LIMIT

sql = "SELECT * FROM 'table name' ORDER BY name"#add DESC to arrange desc
mycursor.execute(sql)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)
#to get data arranged

sql = "DELETE FROM 'table name' WHERE name = .... "
mycursor.execute(sql)
mydb.commit()
#to delete data

sql = "DROP TABLE 'table name'"
mycursor.execute(sql)
mydb.commit()
#to delete a table







































