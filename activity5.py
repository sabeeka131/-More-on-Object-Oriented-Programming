import math
class Circle:
    
    def __init__(self, radius):
        self.radius = radius
    
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    
    def perimeter(self):
        return 2 * math.pi * self.radius


radius_value = float(input("Enter the radius of the circle: "))


circle = Circle(radius_value)


print(f"the area of thecircle is: {circle.area()}")
print(f"tHe perimeter of the circle is: {circle.perimeter()}")