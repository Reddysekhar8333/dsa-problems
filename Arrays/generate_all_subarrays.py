def generate_subarrays(arr):
    n = len(arr)
    subarrays = []

    # Outer loop: Start index
    for start in range(n):
        subarray = []
        # Inner loop: End index
        for end in range(start, n):
            subarray.append(arr[end])  # Extend subarray dynamically
            subarrays.append(subarray[:])  # Store a copy
    
    return subarrays

# Example usage
arr = [1, 2, 3,4]
subarrays = generate_subarrays(arr)

# Print results
for sub in subarrays:
    print(sub)
