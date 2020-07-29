from threading import *
from time import sleep
class mythread:
    
    def displaynumber(self):
        i=0
        print(current_thread().getName())  
        sleep(2)
        while(i<=10):
            print(i)
            i+=1

obj = mythread()
t= Thread(target=obj.displaynumber)
t.start()

t2= Thread(target=obj.displaynumber)
t2.start()

t3= Thread(target=obj.displaynumber)
t3.start()















