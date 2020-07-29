from threading import *

class bookmybus:
    
    def __init__(self,availableseats):
        self.availableseats = availableseats
        self.l = Semaphore()
    
    def buy(self,seatrequested):
        self.l.acquire()
        print('Total seats available',self.availableseats)
        if(self.availableseats>=seatrequested):
            print('confirming a seat')
            print('processing the payment')
            print('printing the ticket')
            self.availableseats-=seatrequested
        else:
            print('sry no seats')
        self.l.release()
    
    
obj = bookmybus(10)
t1 = Thread(target=obj.buy,args=(3,))
t2 = Thread(target=obj.buy,args=(4,))
t3 = Thread(target=obj.buy,args=(4,))

t1.start()
t2.start()
t3.start()
