users = {}

def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    if username in users:
        print("User already exists")
    else:
        users[username] = password
        print("Registered successfully")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful")
    else:
        print("Login failed")

# Example usage
while True:
    choice = input("Choose: register / login / exit: ")
    if choice == "register":
        register()
    elif choice == "login":
        login()
    elif choice == "exit":
        break
    else:
        print("Invalid choice")
