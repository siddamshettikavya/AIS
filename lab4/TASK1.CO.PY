def is_leap_year(year):
    """
    Check if a given year is a leap year.
    Returns True if leap year, otherwise False.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Test cases
print(is_leap_year(2024))  # Expected: True
print(is_leap_year(1900))  # Expected: False
print(is_leap_year(2000))  # Expected: True
print(is_leap_year(2023))  # Expected: False
