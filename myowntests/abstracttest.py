from abc import abstractmethod,ABC


class touchscreenlaptop(ABC): 
        
    def scroll(self):
        pass
    @abstractmethod
    
    def click(self):
        pass
    
class hp(touchscreenlaptop):
    def scroll(self): 
        print('hp is good')
        

class dell(touchscreenlaptop):
    def scroll(self):
        print('dell is good')
        
class hpnotebook(hp):
    def click(self):
        print('hp is awesome')
        
class dellnotebook(dell):
    def click(self):
        print('hp is awesome')
        
hp1=hpnotebook()
hp1.scroll()
hp1.click()

dell2=dellnotebook()
dell2.scroll()
dell2.click()
        
    
    