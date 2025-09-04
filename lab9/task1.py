"""
    Calculates the sum of even and odd numbers in a given iterable.

    Args:
        numbers (iterable of int): A sequence of integers to process.

    Returns:
        tuple: A tuple containing two integers:
            - The sum of even numbers.
            - The sum of odd numbers.

    Example:
        >>> sum_even_odd([1, 2, 3, 4, 5])
        (6, 9)
    """
def sum_even_odd(numbers):
    even_sum = sum(n for n in numbers if n % 2 == 0)
    odd_sum = sum(n for n in numbers if n % 2 != 0)
    return even_sum, odd_sum
a=sum_even_odd([1, 2, 3, 4, 5])
print(a)

#manual documentation
# declare a Function to calculate the sum of even and odd numbers in a list.
#it will Returns the sum of even and odd numbers in the input list.
# Args:
#     numbers (list): List of integers.
#
# Returns:
#     tuple: (sum of even numbers, sum of odd numbers)
# call the function with a sample list and print the result