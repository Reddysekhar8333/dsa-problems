# problem : given an array of positive 'nums' and a positive integer 'target',
#           return the MINIMUM LENGTH of a subarray whose sum is greater than or equal to 'target'.
#           if there is no such subarray ,return 0 instead.   (leetcode 209) 

def min_size_subarray_sum(nums,target):
    n=len(nums)
    min_size = n+1 # we need the max number here.so,size of nums+1 is bigger
    left = 0
    window_sum = 0
    for right in range(n):
        window_sum += nums[right]
        while window_sum >= target:
            min_size = min(min_size,right-left+1) 
            window_sum -= nums[left]
            left += 1
    return 0 if min_size == n+1 else min_size


nums=[2,3,1,2,4,3]
target=7
print(min_size_subarray_sum(nums,target))


