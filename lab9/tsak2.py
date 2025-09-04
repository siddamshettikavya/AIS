# Define a class named sru_student
"""
Module for representing SRU student details and fee status.
Classes:
    sru_student:
        Represents a student at SRU with attributes for name, roll number, hostel status, and fee payment status.
        Methods:
            __init__(name, roll_no, hostel_status):
                Initializes a new student with the given name, roll number, and hostel status. Fee status is set to unpaid by default.
            fee_update(status):
                Updates the fee payment status of the student.
            display_details():
                Displays the student's name, roll number, hostel status, and fee payment status.
"""
class sru_student:
    # Initialize the attributes: name, roll_no, and hostel_status
    def __init__(self, name, roll_no, hostel_status):
        self.name = name  # Store student's name
        self.roll_no = roll_no  # Store student's roll number
        self.hostel_status = hostel_status  # Store hostel status (Yes/No)
        self.fee_paid = False  # Initialize fee status as unpaid

    # Method to update the fee status
    def fee_update(self, status):
        self.fee_paid = status  # Update fee status (True/False)

    # Method to display student details
    def display_details(self):
        print(f"Name: {self.name}")  # Print student's name
        print(f"Roll No: {self.roll_no}")  # Print student's roll number
        print(f"Hostel Status: {self.hostel_status}")  # Print hostel status
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")  # Print fee status

# Create an instance of sru_student
student1 = sru_student("Alice", "101", "TURE")  # Instantiate with sample data

student1.fee_update(True)  # Update fee status to paid

student1.display_details()  # Display all details of the student
#manual documentation
# Define a class named sru_student to represent a student at SRU.
# The class has attributes for the student's name, roll number, hostel status, and fee payment status.
# It includes methods to update the fee status and display the student's details.
# An instance of the class is created with sample data, the fee status is updated, and the details are displayed.
# Define a class named sru_student
# The class has attributes for the student's name, roll number, hostel status, and fee payment status.
# It includes methods to update the fee status and display the student's details.
# An instance of the class is created with sample data, the fee status is updated, and the details are displayed.
