class flight:
    def __init__(self,engine):
        self.engine=engine
        
    def startengine(self):
        self.engine.start();

class airbusengine:
    def start(self):
        print('starting air bus engine')
        
class boingengine:
    def start(self):
        print('starting boingengine engine')
        
ae= airbusengine()
f= flight(ae)
f.startengine()

be= boingengine()
f1= flight(be)
f1.startengine()
