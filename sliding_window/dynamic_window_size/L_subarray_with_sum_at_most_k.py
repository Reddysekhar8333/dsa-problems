# problem : given an array of positive integers 'arr' and an integer 'k',
#           find the length of the longest contiguous subarray such that sum of its elements is <= k.
# Input : 
arr=[1,2,1,0,1,1,0]
k=4
# Output: 5
# Explination: the longest subarray is [1,0,1,1,0] with sum 5 <= K.
def L_subarray_sum_equal_k(arr,k):
    max_len = 0
    left = 0
    window_sum = 0
    for right in range(len(arr)):
        window_sum += arr[right]  
        if window_sum <= k:
            max_len = max(max_len,right-left+1)
        while window_sum > k:
            window_sum -= arr[left]
            max_len = max(max_len,right-left+1)
            left+=1
    return max_len

print(L_subarray_sum_equal_k(arr,k))
