p,s,v,n,m='price:','size:','colors:','Insert details','Enter the code'
import pickle
def inserdata(xe,a,b,c):
    xe=[a,b,c]
    pickle.dump(xe, open('rovandata.dat','wb'))
    print('details saved')
    xe.clear()
#function of code
y=input('what will you do ?:')
if y==('new code'):
    print(n)
    xe=input(m)
    a=input(p)
    b=input(s)
    c=input(v)
    inserdata(xe,a,b,c)
    print('I love you mama')

elif y==('old code'):    
    x=input("Enter the code")
    x = pickle.load(open('rovandata.dat', "rb"))
    print(x)
    print('I love you mama')
else:
    print('Error')
    

