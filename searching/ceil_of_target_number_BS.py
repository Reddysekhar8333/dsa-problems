def ceil_of_target(arr, target):
    "find_smallest_element_greater_than_or_equal_to_target"
    left, right = 0, len(arr) - 1
    result = -1  # Default value if no valid element is found

    while left <= right:
        mid = left + (right - left) // 2  # Avoids overflow
        if arr[mid] >= target:
            result = arr[mid]  # Update result
            right = mid - 1   # Search in the left half for a smaller valid element
        else:
            left = mid + 1    # Search in the right half

    return result

arr = [1, 3, 5, 7, 9, 11, 12, 14, 15, 17, 19, 20]
target = 13
print(ceil_of_target(arr,target))