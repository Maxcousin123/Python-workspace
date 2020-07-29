from abc import abstractmethod,ABC
class bmw(ABC):
    
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    @abstractmethod   
    def start(self):
        pass
        
    @abstractmethod    
    def stop(self):
        pass
    
    @abstractmethod   
    def drive(self):
        pass
    
class threeseries(bmw):
    
    def __init__(self,cruisecontrolenabled,make,model,year):
        super().__init__(make, model, year)
        self.cruisecontrolenabled = cruisecontrolenabled
          
    def display(self):
        print(self.cruisecontrolenabled)
  
    def start(self):
        super().start()
        print('button start')
        
    def stop(self):
        super().stop()
        print('button stop')     
        
   
   
    def drive(self):
        print('three series is being driven')
        
class fiveseries(bmw):
    
    def __init__(self,parkingassistenabled,make,model,year):
        super().__init__(make, model, year)
        self.parkingassistenabled = parkingassistenabled
        
    def start(self):
        super().start()
        print('remote start')
        
    def stop(self):
        super().stop()
        print('remote stop')    
        
 
    def drive(self):
        print('five series is being driven')
 
 
        
bmw=threeseries(True,'bmw','328i','2018')
print(bmw.cruisecontrolenabled)
print(bmw.make)
print(bmw.model)
print(bmw.year)

bmw.start()
bmw.stop()
bmw.display()

bmw2=fiveseries(True,'bmw','328i','2018')





        
        
        