class programmer:
    def setName(self,n):
        self.name=n
    def getName(self):
        return self.name
    
    def setsalary(self,sal):
        self.salary=sal
        
    def getsalary(self):
        return self.salary
    
    def settech(self,techs):
        self.technologies=techs
        
    def gettechnologies(self):
        return self.technologies
    
p1=  programmer()
p1.setName('john')
p1.setsalary(10000)
p1.settech(['java','hibernate','spring','python'])

print(p1.getName())
print(p1.getsalary())
print(p1.gettechnologies())