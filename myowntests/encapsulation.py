class patient:
    
    def setid(self,id):  # @ReservedAssignment
        self.id=id
        
    def getid(self):
        return self.id
    
    def setname(self,name):
        self.name=name
        
    def getname(self):
        return self.name
    
    def setssn(self,ssn):
        self.ssn=ssn
        
    def getssn(self):
        return self.ssn
    
p=patient()
p.setid(123)
p.setssn(456)
p.setname('mohammed')

print(p.getid())
print(p.getname())
print(p.getssn())
