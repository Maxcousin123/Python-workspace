s={10,20,30,"abc",10,20,10}


#set do not allow dublicates
s.update([88,99])
s.remove(30)
print(type(s))
print(s)
#sets do not allow indexing neither subscritable
#and no multiblication

f=frozenset(s)
f.update([20])
#frozen do not allow editing the set