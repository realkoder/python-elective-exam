from circle import Circle

class ColoredCircle(Circle):
    def __init__(self, radius, color):
        super().__init__(radius)
        self.color = color

    def __str__(self):
        return (f"Circle with Radius: {self.radius} and Color: {self.color}")
