class student:
    major='CSE'
    
    def __init__(self,name,roleno):
        self.roleno=roleno
        self.name=name
        
s1=student(1,'john')
s2=student(2,'bill')
print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(student.major)