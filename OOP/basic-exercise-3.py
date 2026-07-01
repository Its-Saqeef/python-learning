#Create a class Rectangle with length and width. Add methods to calculate area and perimeter.

class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area_and_parameter(self):
        area = self.length * self.width
        parameter = 2 * (self.length + self.width)

        print(f"The area of rectangle is {area} and paramter is {parameter}")

rectangle = Rectangle(5,6)
rectangle.area_and_parameter()