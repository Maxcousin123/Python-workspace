x=123
def display():
    y=678
    print(y)
    print(globals()['x'])
    

print(x)

z=display
z()
z()
z()