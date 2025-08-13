# Recursive method
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative method
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
# Built-in method
import math
def factorial_builtin(n):
    return math.factorial(n)

num = 5
print("Recursive:", factorial_recursive(num))
print("Iterative:", factorial_iterative(num))
print("Built-in :", factorial_builtin(num))

