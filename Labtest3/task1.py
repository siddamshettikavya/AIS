def find_min_max(arr, low, high):
    # If there is only one element
    if low == high:
        return arr[low], arr[low]
    # If there are only two elements
    elif high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    else:
        mid = (low + high) // 2
        min1, max1 = find_min_max(arr, low, mid)
        min2, max2 = find_min_max(arr, mid + 1, high)
        return min(min1, min2), max(max1, max2)

# Test with a 12-element list
test_list = [34, 7, 23, 32, 5, 62, 78, 12, 29, 81, 2, 54,100,10]
minimum, maximum = find_min_max(test_list, 0, len(test_list)-1)
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")

