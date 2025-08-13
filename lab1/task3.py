class Student:
    def __init__(self, name, roll_no, age, grade):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.grade = grade

    def display_details(self):
        print("Student Details:")
        print(f"Name     : {self.name}")
        print(f"Roll No. : {self.roll_no}")
        print(f"Age      : {self.age}")
        print(f"Grade    : {self.grade}")

