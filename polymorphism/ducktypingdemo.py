class duck:
    def talk(self):
        print('quack')
        
class human:
    def talk(self):
        print('hello')
        
def calltalk(obj):
    obj.talk();
    
d=duck()
calltalk(d)

h=human()
calltalk(h)