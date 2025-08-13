def calculate_power_bill(units):
    if units <= 100:
        cost = units * 5
    elif units <= 200:
        cost = 100 * 5 + (units - 100) * 7
    else:
        cost = 100 * 5 + 100 * 7 + (units - 200) * 10

    tax = cost * 0.10  # 10% tax
    total = cost + tax
    return cost, tax, total

# Main program
def main():
    try:
        units = int(input("Enter electricity units consumed: "))
        if units < 0:
            print("Units cannot be negative.")
            return

        cost, tax, total = calculate_power_bill(units)

        # Print formatted bill
        print("\n------ Power Bill ------")
        print(f"Units Consumed : {units}")
        print(f"Base Cost      : ₹{cost:.2f}")
        print(f"Tax (10%)      : ₹{tax:.2f}")
        print(f"Total Bill     : ₹{total:.2f}")
        print("------------------------")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
