import random
try:
    z = int(input('how many time u want to play ?'))
    for i in range(z):

        a = input('Pick a choice')
        lst = ['rock','paper','scissors']
        x = random.choice(lst)
        if a == x:
            print('fair')
        elif a=='rock' and x=='paper':
            print('you lose')
            print('computer choice is', x)
        elif a=='paper' and x=='rock':
            print('you win')
            print('computer choice is', x)
        elif a=='rock' and x=='scissors':
            print('you win')
            print('computer choice is', x)
        elif a=='scissors' and x=='rock':
            print('you lose')
            print('computer choice is', x)
        elif a=='scissors' and x=='paper':
            print('you lose')
            print('computer choice is', x)
        elif a=='paper' and x=='scissors':
            print('you lose')
            print('computer choice is', x)
        else:
            print('Error')
except ValueError:
    print('Error')

