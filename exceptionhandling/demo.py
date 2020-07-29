import logging

logging.basicConfig(filename='mylog.log',level=logging.DEBUG)

try:
    f =open('myfile','w')
    a,b=[int(x) for x in input('enter two numbers').split()]
    logging.info('division in progress')
    c=a/b
    f.write('writing %d into file' %c)
except ZeroDivisionError:
    print('division by zero is not allowed')
    print('plear enter a new num')
    logging.error('division by zero')
else:   
    print('u have entered the non zero number')
finally:
    f.close()
    print('file closed')
print('code after the exception')
