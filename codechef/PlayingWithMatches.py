c = int(input())
for i in range(c):
    a,b=map(int,input().split())
    y = a + b
    l = []
    while (y != 0):
        n = y % 10
        if(n==0 or n==9):
            l.append(6)
        elif(n==1):
            l.append(2)
        elif(n==2 or n==3 or n==5):
            l.append(5)
        elif(n==4):
            l.append(4)
        elif(n==6):
            l.append(6)
        elif(n==7):
            l.append(3)
        else:
            l.append(7)
        y=y//10
    print(sum(l))