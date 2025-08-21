
def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

# Example run
print("Sum using while loop:", sum_to_n_while(10))
def sum_to_n_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

