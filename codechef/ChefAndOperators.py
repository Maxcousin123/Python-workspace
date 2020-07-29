z=int(input('m'))

for i in range(z):
    x,y=map(int,input('l').split())
    if x > y :
        print('>')
    elif x < y :
        print('<')
    else:
        print('=')
        

