lst=[10,20,'moh',-10,30,5]
print(lst)
print(lst[3])
print(lst[3:5])
print(lst*4)
print(len(lst))

lst.append(40)
print(lst)
lst.remove('moh')
del(lst[1])

#lst.clear()
#print(lst)

print(max(lst))
print(min(lst))

lst.insert(3,99)
print(lst)

lst.sort(reverse=True)
print(lst)


