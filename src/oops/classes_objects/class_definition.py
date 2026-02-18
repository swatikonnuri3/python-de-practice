class Student:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")