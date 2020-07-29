import mysql.connector
x,y,z,v='color: ','size: ','price: ','Enter the code: '
mydb = mysql.connector.connect(
    host='localhost',
    user='maxcousin',
    password='secret :)',
    database='testdb' #to request a specific database
    )
mycursor = mydb.cursor()

def newdata(b,c,d,e):
    """to insert the code and data"""
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM rovan WHERE code=(%s) ',(b,));
    myresult = mycursor.fetchall()
    
    if len(myresult) > 1:
        print('code already exists')
        
        
    else:
        mycursor = mydb.cursor()
        sqlFormula = "INSERT INTO rovan (code, size, price, color) VALUES (%s, %s, %s ,%s)"
        rovan1 = (b, d, e, c)
        mycursor.execute(sqlFormula, rovan1)
        mydb.commit()
        print('Done !')
def olddata(g):
    '''to get the data related to code'''
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM rovan WHERE code=(%s)",(g,));
        myresult = mycursor.fetchall()
        for result in myresult:
            print(result)
    except:
        print('Error')    
def editcode(f):
    i = input('what will you edit ?: ')
    if i == ('price'):
        j = input("Enter the new price: ")
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE rovan SET price=(%s) WHERE code=(%s)",(j,f));
        mydb.commit()
        print('Done')
    elif i == ('size'):
        k = input('Enter the sizes: ')
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE rovan SET size=(%s) WHERE code=(%s)",(k,f));
        mydb.commit()
        print('Done')
    elif i == ('color'):
        l = ('Enter the colors: ')
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE rovan SET color=(%s) WHERE code=(%s)",(l,f));
        mydb.commit()
        print('Done')
    else:
        print('Wrong command')
def delcode(h):
    try:
        mycursor.execute("DELETE FROM rovan WHERE code=(%s)",(h,));
        mydb.commit()    
        print('Done !')
    except:
        print("Error")
a = input('What will you do ?: ')

if a == 'new code':
    b = int(input(v))
    c = input(x)
    d = input(y)
    e = input(z)
    newdata(b,c,d,e)
elif a == 'edit code':
    f = input(v)
    editcode(f)    
elif a == 'old code':
    g = input(v)
    olddata(g)
elif a == 'delete code':
    h = input(v)
    delcode(h)
else:
    print('Wrong command')
    
