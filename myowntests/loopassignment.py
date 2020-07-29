x=int(input('Enter a number'))
y=0
i=y
while y<x:
    y+=1
    if(y>100):
        break
    if y % 10 ==0:
        continue
    
    print(y)
