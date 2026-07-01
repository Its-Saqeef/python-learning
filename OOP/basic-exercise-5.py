#Create a class Circle with radius. Add a method to calculate area.

import math

class Circle():
    def __init__(self, radius):

        area = math.pi * radius**2
        print(f"The area of circle is : {area:.2f}")

circle = Circle(10)