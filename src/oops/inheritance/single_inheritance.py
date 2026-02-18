class Person:
    def role(self):
        print("I am a person")

class Employee(Person):
    def role(self):
        print("I am an employee")

emp = Employee()
emp.role()