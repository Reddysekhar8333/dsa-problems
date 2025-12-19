# Problem: Subarray Sum Equals K (LeetCode 560)

# Given: an integer array nums and an integer k
# Return: how many subarrays have sum = k

def subarray_sum(nums,k):
    count = 0
    prefix = 0 
    freq = {0:1}
    for i in range(len(nums)):
        prefix += nums[i]
        if prefix-k in freq:
            count += freq[prefix-k] 
        freq[prefix] = freq.get(prefix,0)+1
    return count

nums=[1,2,-3,1,2,-6,1,2,3]
k=3
print(subarray_sum(nums,k))
