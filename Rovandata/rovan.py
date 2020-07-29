import mysql.connector
from tkinter import *
x,y,z,v='color: ','size: ','price: ','Enter the code: '


mydb = mysql.connector.connect(
    host='localhost',
    user='maxcousin',
    password='www.moh.com',
    database='testdb' #to request a specific database
    )
mycursor = mydb.cursor()
lst = []
def newdata(b,c,d,e):
    """to insert the code and data"""
    
    mycursor = mydb.cursor()
    mycursor.execute('SELECT code=(%s) FROM rovan',(b,));
    myresult = mycursor.fetchall()
    for g in myresult:
        lst.append(g)
    if len(lst) > 1:
        la = Label(root, text='Code already exists')
        la.pack()

    else:
        mycursor = mydb.cursor()
        sqlFormula = "INSERT INTO rovan (code, size, price, color) VALUES (%s, %s, %s ,%s)"
        rovan1 = (b, d, e, c)
        mycursor.execute(sqlFormula, rovan1)
        mydb.commit()
        la2 = Label(root, text='Done !')
        la2.pack()
 
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

root = Tk()
root.geometry('400x400')





en = Entry(root, width=50, borderwidth=5)
en.pack()
en.insert(0, 'Code:')
en2 = Entry(root, width=50, borderwidth=5)
en2.pack()
en2.insert(0, 'price:')
en3 = Entry(root, width=50, borderwidth=5)
en3.pack()
en3.insert(0, 'size:')
en4 = Entry(root,  width=50, borderwidth=5)
en4.pack()
en4.insert(0, 'color:')

nt = en.get()
nt2 = en2.get()
nt3 = en3.get()
nt4 = en4.get()





bt2 = Button(root, text = 'old code')
bt2.pack()
bt3 = Button(root, text = 'edit code')
bt3.pack()
bt4 = Button(root, text = 'delete code')            
bt4.pack()
la3 = Label(root, text='...')
la3.pack()


def newdata1(nt,nt2,nt3,nt4):
    
    b = nt
    c = nt4
    d = nt3
    e = nt2
    return newdata(b, c, d, e)

bt = Button(root, text = 'new code', command = newdata1(nt,nt2,nt3,nt4))
bt.pack()

root.mainloop()




    
    














