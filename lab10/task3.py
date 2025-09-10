class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def increase(self, percent: float) -> None:
        self.salary = self.salary + (self.salary * percent / 100)

    def print_info(self) -> None:
        print(f"emp: {self.name} salary: {self.salary}")


employees = [
    (Employee("kavya", 1000), 10),
    (Employee("deeksha", 2000), 20),
    (Employee("laxmi", 3000), 30),
]

for employee, percent in employees:
    employee.increase(percent)
    employee.print_info()
