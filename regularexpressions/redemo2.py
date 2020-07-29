import re
str = 'Take up One idea.One idea at a time'
result = re.search(r'o\w',str)
print(result)
#group is for value coming from search
result = re.findall(r'o\w\w',str)
print(result)

result = re.match(r'T\w\w',str)
print(result)

result = re.sub(r'one', 'two', str)
print(result)

result = re.findall(r'0\w{1,2}',str)
print(result)

result = re.split(r'\d+',str)
print(result)