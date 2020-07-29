from threading import *

from time import *

class EvenThread:

    def evenNumbers(self):

        print(current_thread().getName())

for i in range(1,101):

    if i%2==0:

        print(i)

class OddThread:

    def oddNumbers(self):

        print(current_thread().getName())

for i in range(1,101):

    if i%2!=0:

        print(i)

obj1 = EvenNumbers

obj2 = OddNumbers

t1 = Thread(target = obj1.evenNumbers)

t2 = Thread(target = obj2.oddNumbers)

t1.start()

sleep(1)

t2.start()

sleep(1)

print(current_thread().getName())