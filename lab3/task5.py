def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def main():
    while True:
        print("\n🌡️ Temperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '3':
            print("👋 Exiting the program. Goodbye!")
            break

        if choice not in ['1', '2']:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
            continue

        try:
            temp = float(input("Enter the temperature to convert: "))
            if choice == '1':
                result = celsius_to_fahrenheit(temp)
                print(f"✅ {temp}°C = {result:.2f}°F")
            else:
                result = fahrenheit_to_celsius(temp)
                print(f"✅ {temp}°F = {result:.2f}°C")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

# Run the program
main()
