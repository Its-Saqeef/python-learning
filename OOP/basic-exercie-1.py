#Create a class Car with attributes brand, model, and year. Create an object and print its details.
#Add a method display_info() to the Car class that prints all attributes.

class Car():
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"The brand is {self.brand},model is {self.model} and year is {self.year}")

obj = Car("Toyota","Corolla","2018")

obj.display_info()