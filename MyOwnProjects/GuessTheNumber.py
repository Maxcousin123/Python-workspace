import random
def number(z,x):
    if abs(z-x) and (z-x) == 1:
        print('too close')
        print('this is the correct number ',x)
    elif abs(z-x) and (z-x) ==2:
        print('close')
        print('this is the correct number ',x)
    elif abs(z-x) and (z-x) ==3:
        print('not close')
        print('this is the correct number ',x)
    elif abs(z-x) and (z-x) ==4:
        print('far')
        print('this is the correct number ',x)
    elif z == x:
        print('correct :)')
    else:
        print('too far')
        print('this is the correct number ',x)
def notallowed(z):
    if z > 20:
        print('this not allowed')
    elif z <= 20:
        number(z,x)
try :
    y = int(input('How many guesses you want ?'))
    for i in range(y):
        x = (random.randrange(20))
        z = int(input('Number is created , guess it'))
        notallowed(z)
    else:
        print('Finished')
except ValueError:
    print('Please Enter a valid number')
    
