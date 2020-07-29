x = int(input())

for i in range(x):
    s1 = input()
    s2 = input()

    c=0
    p=0
    
    for i in range(0,len(s1)):
        if(s1[i]!='?' and s2[i]!='?' and s1[i]!=s2[i]):
            c=c+1
        if(s1[i]=='?' or s2[i]=='?' or s1[i]!=s2[i]):
            p=p+1
    
    print(c,p)
    