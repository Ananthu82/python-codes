class shape:
    def area(self):
        print("calculating area")
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f"area of circle : {3.14*self.radius**2}")
class rectangle(shape):
    def __init__(self,lenght,breadth):
        self.lenght=lenght
        self.breadth=breadth
    def area(self):
        print(f"area of rectangle : {self.lenght*self.breadth}")
circle_area=circle(4)
rectangle_area=rectangle(3,5)
circle_area.area()
rectangle_area.area()