'''from tkinter import *

root = Tk()#to make the window
root.geometry('300x300')#to make the size of the window 

c = Canvas(root, height=250, width=300, bg='blue')#to make a paint window 
c.pack()

r= c.create_rectangle(20,20,100,100,fill='red')

l1 = c.create_line(5,5,200,200, width = 10)

o = c.create_oval(20,20,100,200,fill='red')

arc = c.create_arc(10,50,240,210, extent=260, fill='red')

l = Label(root, text='Hello world')
l.pack()



def buttonfun():
    print('Hello world')
    

                                   #this to make button function
b = Button(root, text='Click me !', command = buttonfun)
b.pack()#pack sort the elements 

b2 = Button(root, text='Click me !', command = buttonfun)
b2.pack(side=LEFT)#to sort elements side by side
#BOTTOM , TOP , RIGHT







root.mainloop()#to make the window stay'''

'''from tkinter import *

root = Tk()
root.geometry('300x300')

mb = Menubutton(root, text='This is a menu')
mb.menu = Menu(mb)
mb['menu'] = mb.menu

mb.menu.add_command(label='Option 1', command= lambda: print('This is option 1'))

def func1():
    print('This is a option') #the above command saves time to write this function

mb.menu.add_command(label='Option 2', command= lambda: print('This is option 2'))
mb.pack()

root.mainloop()

from tkinter import *
import tkinter as tk
root =Tk()
root.geometry('300x300')

v = tk.IntVar()

                                 # this is used to store value in v
radiobutton1 = Radiobutton(root, variable = v , value = 0,text = 'It is sunny', command=lambda: print(v.get()))
radiobutton2 = Radiobutton(root, variable = v , value = 1, text = 'It is rainy', command=lambda: print(v.get()))

radiobutton1.pack()
radiobutton2.pack()

root.mainloop()
'''
from tkinter import *

 
root = Tk()

#fg for foreground
e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter your name:")
def myClick():
    hello = 'hello ' + e.get()
    mylabel = Label(root, text =hello)
    mylabel.pack()
    
mybutton = Button(root, text='Click me!',command=myClick)
mybutton.pack()

root.mainloop()




















