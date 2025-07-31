def find_max_of_three(numbers):
    """Return the maximum element from a list of 3 numbers."""
    return max(numbers)

if __name__ == "__main__":
    nums = []
    for i in range(3):
        num = float(input(f"Enter number {i+1}: "))
        nums.append(num)
    maximum = find_max_of_three(nums)
    print(f"The maximum element is: {maximum}")
