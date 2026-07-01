#Create a class Student with attributes name and marks. Add a method to print if the student passed (marks ≥ 40).

class Student():
    def __init__(self,marks,name):
        self.marks = marks
        self.name = name
    
    def is_pass(self):
        if self.marks >= 40:
            print(f"{self.name} is Pass")
        else:
            print(f"{self.name} is Fail")

student = Student(30,"Ahmad")
student.is_pass()