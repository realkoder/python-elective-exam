import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)
    
    def calculate_perimeter(self):
        return round(2 * math.pi * self.radius, 2)
    
    def calculate_diameter(self):
        return round(2 * self.radius, 2)

    def calculate_area_2_circles(self, circle2):
        return self.calculate_area() + circle2.calculate_area()
    
    

