def floor_of_target(arr, target):
    "find_greatest_element_less_than_or_equal_to_target"
    left, right = 0, len(arr) - 1
    result = -1  # Default value if no valid element is found

    while left <= right:
        mid = left + (right -left) // 2  # Avoids overflow
        if arr[mid] <= target: 
            result = arr[mid]  # Update result
            left = mid + 1    # Search in the right half for a larger valid element
        else:
            right = mid - 1   # Search in the left half

    return result

arr = [1, 3, 5, 7, 9, 11, 12 ]
target = 8
print(floor_of_target(arr,target))