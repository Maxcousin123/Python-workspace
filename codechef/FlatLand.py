for j in range(int(input('n'))):
    n=int(input('x'))
    count = 0
    while n>0:
        j = int(n**(1/2))
        n = (n)-(j**2)
        count += 1
    print(count)
    
    