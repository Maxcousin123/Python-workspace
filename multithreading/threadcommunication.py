from threading import *;
from time import *;

class producer:
    def __init__(self):
        self.products = []
        self.ordersplaced = False
        
    def produce(self):
        for i in range(1,5):
            self.products.append('product'+str(i))
            sleep(1)
            print('Item Added')
        self.ordersplaced = True    
        
class consumer:
    def __init__(self,prod):
        self.prod = prod
        
        def consume(self):
            
            while self.prod.ordersplaced == False:
                print('waiting for the orders')
                sleep(0.2)
            
            print('Orders shipped',self.prod.products)
        
        
p = producer()
c=consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()
        
        
        
        
        
        
        