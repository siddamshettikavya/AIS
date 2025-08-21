
while True:
    age = int(input("Enter your age (or -1 to exit): "))
    if age == -1:   # Exit condition
        print("Exiting program...")
        break

    if age < 0:
        print("Invalid age entered.")
    elif age < 13:
        print("You are a Child.")
    elif age <= 19:
        print("You are a Teenager.")
    elif age <= 59:
        print("You are an Adult.")
    else:
        print("You are a Senior.")
        
    
