import mysql.connector
from tkinter import *


mydb = mysql.connector.connect(
    host='localhost',
    user='maxcousin',
    password='secret :)',
    database='testdb' #to request a specific database
    )

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
def er():
    la = Label(root, text = 'code already exists')
    la.pack


mycursor = mydb.cursor()
def newdata(nt,nt2,nt3,nt4):
    """to insert the code and data"""
    
 
     
    lst = []
    mycursor = mydb.cursor()
    mycursor.execute('SELECT code=(%s) FROM rovan',(nt,));
    myresult = mycursor.fetchall()
    for g in myresult:
        lst.append(g)
    if len(lst) > 1:
        er()
    else:
        mycursor = mydb.cursor()
        sqlFormula = "INSERT INTO rovan (code, size, price, color) VALUES (%s, %s, %s ,%s)"
        rovan1 = (nt, nt3, nt2, nt4)
        mycursor.execute(sqlFormula, rovan1)
        mydb.commit()
        #put output
bt = Button(root, text='new code', command = newdata(nt,nt2,nt3,nt4))
bt.pack(side=LEFT)
def olddata(g):
    '''to get the data related to code'''
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM rovan WHERE code=(%s)",(g,));
        myresult = mycursor.fetchall()
        for result in myresult:
            print(result)
    except:
        print('ss')  # !
def editcode(f):
    i = input('what will you edit ?: ')
    if i == ('price'):
        j = input("Enter the new price: ")
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE rovan SET price=(%s) WHERE code=(%s)",(j,f));
        mydb.commit()
        #put output
    elif i == ('size'):
        k = input('Enter the sizes: ')
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE rovan SET size=(%s) WHERE code=(%s)",(k,f));
        mydb.commit()
        #put output
    elif i == ('color'):
        l = ('Enter the colors: ')
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE rovan SET color=(%s) WHERE code=(%s)",(l,f));
        mydb.commit()
        #put output
    else:
        print('put output here')# !
def delcode(h):
    try:
        mycursor.execute("DELETE FROM rovan WHERE code=(%s)",(h,));
        mydb.commit()    
        #put output
    except:
        print('put output here')# !
root.mainloop()