# Given an array of integers and a value 'k',
# return the longest subarray length whose sum equals 'k'.
# a subarray is a contiguous non-empty sequences of elements in the array.

def longest_subarray_sum(nums,k):
    prefix_map = {0:-1}
    resultMax = 0
    prefixSum = 0

    for i, num in enumerate(nums):
        prefixSum += num
        # check if we have seen (prefixSum - k)
        if (prefixSum - k) in prefix_map:
            length = i - prefix_map[prefixSum - k]
            resultMax = max(resultMax,length)
        # store only first seen prefix sum
        if prefixSum not in prefix_map:
            prefix_map[prefixSum] = i

    return resultMax

nums=[5,2,2,5,1,1,1,1,4]
k=4
print(longest_subarray_sum(nums,k))