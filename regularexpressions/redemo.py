import re
str = 'Take 1 up one 23 idea.One idea 45 at a time 12-11-2020'
result = re.search(r'o\w',str)
print(result)
#group is for value coming from search
result = re.findall(r'o\w\w',str)
print(result)

result = re.match(r'T\w\w',str)
print(result)#putting group() write the letter direct

result = re.sub(r'one','two',str)
print(result)

result = re.findall(r'O\w{1,2}?',str)
print(result)

result=re.split(r'\d+',str)
print(result)

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(result)

result = re.search(r'^T\w*',str)
print(result.group())








