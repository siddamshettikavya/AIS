
def print_multiples_while(n):
    print(f"First 10 multiples of {n} (using while loop):")
    i = 1
    while i <= 10:   # Loop until 10
        print(n * i)
        i += 1
# Function to print first 10 multiples using a FOR loop
def print_multiples_for(n):
    print(f"First 10 multiples of {n} (using for loop):")
    for i in range(1, 11):  # Loop from 1 to 10
        print(n * i)
# Example run
print_multiples_for(5)