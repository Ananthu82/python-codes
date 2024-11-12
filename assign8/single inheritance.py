class vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def drive(self):
        pass
class car(vehicle):
    def __init__(self,brand,speed,fuel_type):
        super().__init__(brand,speed)
        self.fuel_type=fuel_type
    def details(self):
        return f"brand : {self.brand} , speed : {self.speed} , fuel type : {self.fuel_type}"
car1=car("volkswagen",210,"petrol")
print(car1.details())