#Create a class Employee with attributes name and salary. Add a method to increase salary by a percentage.

class Employee():
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def salary_increment(self,percentage):
        if self.salary > 0:
            self.salary = self.salary + ((percentage / 100) * self.salary )
            print(f"New salary is : {self.salary}")
    
employee = Employee("Ahmad",50000)
employee.salary_increment(10)
