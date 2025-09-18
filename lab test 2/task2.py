def avg_yield_per_acre(total_yield: float, acres: float) -> float:
    """
    Calculate the average crop yield per acre.
    
    This function computes the average crop yield by dividing the total yield
    by the number of acres. It's commonly used in agritech analytics to assess
    agricultural productivity and efficiency.
    
    Args:
        total_yield (float): The total crop yield in units (e.g., bushels, tons).
                            Must be a non-negative numeric value.
        acres (float): The total number of acres of farmland.
                      Must be a positive numeric value.
    
    Returns:
        float: The average crop yield per acre. Returns 0.0 if acres is 0.
    
    Raises:
        ZeroDivisionError: If acres is 0, division by zero will occur.
        TypeError: If either parameter is not numeric.
        ValueError: If either parameter is negative.
    
    Example:
        >>> avg_yield_per_acre(500, 50)
        10.0
        >>> avg_yield_per_acre(1000, 25)
        40.0
        >>> avg_yield_per_acre(0, 10)
        0.0
    
    Note:
        Edge cases to consider:
        - Division by zero: If acres is 0, this will raise ZeroDivisionError
        - Negative values: Function assumes non-negative total_yield and positive acres
        - Zero total yield: Returns 0.0 regardless of acres (as long as acres > 0)
        - Input validation: Consider adding type checking for production use
    """
    if acres == 0:
        raise ZeroDivisionError("Cannot divide by zero: acres must be greater than 0")
    
    if not isinstance(total_yield, (int, float)) or not isinstance(acres, (int, float)):
        raise TypeError("Both total_yield and acres must be numeric values")
    
    if total_yield < 0:
        raise ValueError("total_yield must be non-negative")
    
    if acres < 0:
        raise ValueError("acres must be positive")
    
    return total_yield / acres


# Test the function with the provided sample
if __name__ == "__main__":
    # Test with the provided sample
    print("Sample test:")
    print(f"avg_yield_per_acre(500, 50) = {avg_yield_per_acre(500, 50)}")
    
    # Additional test cases
    print("\nAdditional test cases:")
    
    # Test case 1: Normal case
    print(f"avg_yield_per_acre(1000, 25) = {avg_yield_per_acre(1000, 25)}")
    
    # Test case 2: Zero yield
    print(f"avg_yield_per_acre(0, 10) = {avg_yield_per_acre(0, 10)}")
    
    # Test case 3: Decimal values
    print(f"avg_yield_per_acre(750.5, 30.2) = {avg_yield_per_acre(750.5, 30.2)}")
    
    # Test case 4: Edge case - division by zero (commented out to avoid error)
    # print(f"avg_yield_per_acre(500, 0) = {avg_yield_per_acre(500, 0)}")
    print("Edge case - division by zero:")
    try:
        avg_yield_per_acre(500, 0)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    
    # Test case 5: Invalid input types (commented out to avoid error)
    # print(f"avg_yield_per_acre('500', 50) = {avg_yield_per_acre('500', 50)}")
    print("Edge case - invalid input type:")
    try:
        avg_yield_per_acre('500', 50)
    except TypeError as e:
        print(f"Error: {e}")
print(avg_yield_per_acre(500, 50))  # Output: 10.0
print(avg_yield_per_acre(1000,25))  # Output: 40.0
print(avg_yield_per_acre(0,10))  # Output: 0.0
print(avg_yield_per_acre(750.5, 30.2))  # Output: 24.835761589403973