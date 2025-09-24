class Student:
    def __init__(self, name, age, mark1, mark2, mark3):
        self.name = name
        self.age = age
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def details(self):
        print("Name:", self.name, "Age:", self.age)

    def total(self):
        return self.mark1 + self.mark2 + self.mark3
if __name__ == "__main__":
    student = Student("Alice", 20, 85, 90, 88)
    student.details()
    print("Total:", student.total())


