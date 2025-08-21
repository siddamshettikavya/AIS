class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.rollno = roll_no   # corrected variable name
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Marks: {self.marks}")

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "Fail"

    def display_grade(self):
        grade = self.calculate_grade()
        print(f"Grade: {grade}")
        if grade == "Fail":
            print("You need to improve your marks.")
        else:
            print("Congratulations! You have passed.")


# Example usage:
student1 = Student("Kavya", 101, 85)
student1.display_details()
student1.display_grade()
# Example usage:
student2 = Student("Rahul", 102, 55)
student2.display_details()
student2.display_grade()
# Example usage:
student3 = Student("Anita", 103, 92)
student3.display_details()
student3.display_grade()
