# A subarray is a contiguous part of an array.
def find_all_subarrays(arr):
    n = len(arr)
    subarrays = []
    for start in range(n):
        for end in range(start,n):
            subarrays.append(arr[start:end+1])
    return subarrays

# Example
arr = [1, 2, 3]
result = find_all_subarrays(arr)
print("All subarrays:", result)
print("Total subarrays:", len(result))