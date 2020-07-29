from functools import reduce

lst=[5,10,15,20]
result=reduce(lambda x,y:x+y, lst)
print(result)
#this is used to find sum of all things in the list