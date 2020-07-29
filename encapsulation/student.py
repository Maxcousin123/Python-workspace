'''class student:
    def __init__(self):
        self.__id=123
        self.__name='john'
        
    def display(self):
        print(self.__id)
        print(self.__name)
        
#u make an object hidden with __        
        
s = student()
s.display()
#u can access hidden objects
print(s._student__id);
print(s._student__name);
#this is called name mangling'''

class student:
    def setid(self,id):  # @ReservedAssignment
        self.id=id
    def getid(self):
        return self.id
    
    def setname(self,name):
        self.name =name
        
    def getname(self):
        return self.name
        
        
s=student()
s.setid(123)
s.setname('john')
print(s.getid())
print(s.getname())
        
        
        
        
        
        
        
        
        
        
        
        