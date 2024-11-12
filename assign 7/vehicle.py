class vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def start(self):
        print("the vehicle is starting")
class car(vehicle):
    def __init__(self,make,model,fuel_type):
        super().__init__(make,model) 
        self.fuel_type=fuel_type

    def start(self):
        print(f"the car is starting with {self.fuel_type} fuel")   
car1=car("bmw",1997,"petrol")
car1.start()