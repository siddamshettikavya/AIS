def centimeters_to_inches(centimeters):
    """
    Convert centimeters to inches.

    Args:
        centimeters (float): The length in centimeters.

    Returns:
        float: The length in inches.
    """
    return centimeters / 2.54
inches = centimeters_to_inches(10)
print(inches)  # Output: