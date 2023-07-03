#### LESS 15

##Task 15_1
class Transport(object):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def prn(self):
        print(f"Nazvanie avto: {self.name}. Ckorost:{self.max_speed}. Probeg: {self.mileage}." )

Autobus=Transport('Renaul Logan',180,12)
Autobus.prn()


##Task 15_1
class Transport(object):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def prn(self):
        print(f"Nazvanie avto: {self.name}. Ckorost:{self.max_speed}. Probeg: {self.mileage}." )

class Autobus(Transport):
   def __init__(self,name, max_speed, mileage,capacity=50):
       super().__init__(name, max_speed, mileage)
       self.seating_capacity=capacity
   def prn(self):
       print(f"Nazvanie avto: {self.name}. Ckorost:{self.max_speed}. Probeg: {self.mileage}. Sidyachih mest: {self.seating_capacity}" )
    
a=Autobus('Renaul Logan',180,12)
a.prn()